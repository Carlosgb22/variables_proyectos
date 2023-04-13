from odoo import fields, models

class Permisos(models.Model):
    #Nombre del modelo
    _name = "proyecto.permiso"
    #Nombre
    _rec_name = "usuario"
    #Descripcion del modelo
    _description = "Permiso de lectura o escritura en el proyecto"
    usuario = fields.Many2one('res.users', string='Usuarios', tracking=True, required=True)
    permiso = fields.Selection([("lectura", "Lectura"), ("escritura", "Escritura")], string = "Permiso", required = True, tracking=True, ondelete='set default')
