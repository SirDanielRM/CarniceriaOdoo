from odoo import models, fields, api

class Ofertas (models.Model):
    _name= 'carniceria.ofertas'
    codOferta = fields.Integer('Codigo Oferta', required = True)
    newPrecio = fields.Float('Precio en Oferta', required = True)
    descrip = fields.Char('Descripcion de la Oferta', required = False)
    carne = fields.Many2one('carniceria.carnes', 'Nombre del Producto')
    activo = fields.Boolean('Esta activa la oferta?')

    @api.one
    def limpiar(self):
	self.activo = False

