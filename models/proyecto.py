# -*- coding: utf-8 -*-
from odoo import api, fields, models

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
    variables = fields.Many2many("variable", string = "Variables", tracking=True, groups="variables_proyectos.proyecto_user_group")
