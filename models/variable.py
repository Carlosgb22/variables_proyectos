# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models

class Variable(models.Model):
    #Nombre del modelo
    _name="variable"
    #Descripcion del modelo
    _description="Variable"
    _rec_name = "nombre"
    _inherit = ['mail.thread','mail.activity.mixin']

    #Campos del modelo
    nombre=fields.Char(string="Nombre", required=True, tracking=True)
    valor=fields.Char(string="Valor", required=True, tracking=True)
    valor2=fields.Char(string="Valor", required=True, tracking=True, related="valor")
    descripcion=fields.Char(string="Descripción", tracking=True)
    secreto=fields.Boolean(string="Secreto", tracking=True)
    recordatorio=fields.Datetime(string="Recordatorio", required=True, tracking=True)
    categoria=fields.Many2one("variable.categoria", string="Categoria", tracking=True)

class VariableRecordatorio(models.Model):
    _name = 'variable.recordatorio'
    _description = 'Modelo para enviar recordatorios'
    inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def send_reminder_notification(self):
        today = datetime.now().date()
        variables = self.env['variable'].search([('recordatorio', '<', today)])
        for variable in variables:
            #variable.message_subscribe
            follower_names = self.env['mail.followers'].search([('res_model', '=', 'variable'), ('res_id', '=', variable.id)]).mapped('partner_id').mapped("name")
            for follower in follower_names:
                message ="La variable %s ha caducado el dia %s. Revisala por favor %s"%(variable.nombre, variable.recordatorio, follower)
                variable.message_post(body=message, subject="Recordatorio")
