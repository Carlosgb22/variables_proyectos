# -*- coding: utf-8 -*-
from random import randint

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProyectoCategoria(models.Model):
    #Nombre del modelo
    _name = "proyecto.categoria"
    #Nombre categoría
    _rec_name = "nombre"
    #Descripcion del modelo
    _description = "Categoria de Proyectos"

    #Metodo que devuelve un numero aleatorio
    def _get_default_color(self):
        return randint(1, 11)

    #Metodo que compueba que no existan dos nombres de categoria de proyecto iguales
    @api.constrains('nombre')
    def comprobar_nombre_unico(self):
        if self.nombre and self.nombre != '':
            categorias = self.env['proyecto.categoria'].search([('nombre','=',self.nombre)])
        if len(categorias) > 1:
            raise ValidationError('Ya existen categorias con el nombre %s'%(self.nombre))

    #Campos del modelo
    nombre = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string='Color', default=_get_default_color)