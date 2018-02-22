from odoo import models, fields

class proveedores (models.Model):
    _name = 'carniceria.proveedores'
    codProv = fields.Integer('Codigo del Proveedor', required = True)
    nomProv = fields.Char('Nombre del Proveedor', required = True)
    telefono = fields.Integer('Numero de telefono', required = True)
    direccion = fields.Char('Direccion', required = False)
