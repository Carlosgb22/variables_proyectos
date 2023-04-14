# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Proyecto(models.Model):
    #Nombre del modelo
    _name = "proyecto"
    #Nombre proyecto
    _rec_name = "nombre"
    #Descripcion del modelo
    _description = "Proyecto"
    _inherit = ['mail.thread']

    #Campos del modelo
    nombre = fields.Char(string = "Nombre", required = True, tracking=True)
    categoria = fields.Many2many("proyecto.categoria", string = "Categoria", tracking=True)
    estado = fields.Selection([
        ("desarrollo", "Desarrollo"),
        ("produccion", "Produccion"),
        ("finalizado", "Finalizado"),
    ], string = "Estado", default = "desarrollo", required = True, tracking=True, ondelete='set default')
    permisos = fields.Many2many('proyecto.permiso', string='Usuarios', tracking=True)
    variables = fields.Many2many("variable", string = "Variables", tracking=True)
    comprobacion=fields.Boolean(string="Comprobacion", tracking=True, compute='check_edit')
    comprobacion_grupo=fields.Boolean(string="id", compute='is_user')

    @api.depends('permisos', 'permisos.permiso', 'permisos.usuario')
    def is_user(self):
        check_2 = False
        for rec in self:
            if rec.permisos.usuario.id == self.env.user.id:
                check_2=True
        rec.comprobacion_grupo= check_2


    @api.depends('permisos', 'permisos.permiso', 'permisos.usuario')
    def check_edit(self):
        check = False
        for roc in self:
            for ric in roc.permisos:
                if ric.usuario.id==self.env.user.id and not check:
                    if ric.permiso=="escritura":
                        check=True
            roc.comprobacion = check

    #Metodo para comprobar que no existan 2 categorias de variable con el mismo nombre
    _sql_constraints=[
        ('name_uniq', 'unique (nombre)', "Ya existe una categoría con ese nombre")
    ]