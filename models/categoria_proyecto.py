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

    #Metodo para comprobar que no existan 2 categorias de variable con el mismo nombre
    _sql_constraints=[
        ('name_uniq', 'unique (nombre)', "Ya existe una categoría con ese nombre")
    ]

    #Campos del modelo
    nombre = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string='Color', default=_get_default_color)