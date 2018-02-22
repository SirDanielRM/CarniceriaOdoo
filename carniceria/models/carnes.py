from odoo import models, fields

class carnes(models.Model):
    _name='carniceria.carnes'
    codCarne = fields.Integer('Codigo de la Carne', required = True)
    nomCarne = fields.Char('Nombre de Carne', requiered = True)
    typeCarne = fields.Many2one('carniceria.tipos', 'Tipos de Carne')
    precio = fields.Char('Precio del Producto', required = True)

    def name_get(self):
        res=[]
        for record in self:
            nameC = record.nomCarne
            res.append((record.id, nameC))
	return res
