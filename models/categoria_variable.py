# -*- coding: utf-8 -*-
from random import randint

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class VariableCategoria(models.Model):
    #Nombre del modelo
    _name = "variable.categoria"
    #Nombre categoría
    _rec_name = "nombre"
    #Descripcion del modelo
    _description = "Categoria de Variables"

    #Metodo que devuelve un numero aleatorio
    def _get_default_color(self):
        return randint(1, 11)

    #Metodo para comprobar que no existan 2 categorias de variable con el mismo nombre
    @api.constrains('nombre')
    def comprobar_nombre_unico(self):
        if self.nombre and self.nombre != '':
            categorias = self.env['variable.categoria'].search([('nombre','=',self.nombre)])
        if len(categorias) > 1:
            raise ValidationError('Ya existen categorias con el nombre %s'%(self.nombre))

    #Campos del modelo
    nombre = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string='Color', default=_get_default_color)