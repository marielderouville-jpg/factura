from odoo import models, fields


class Factura(models.Model):
    _name = 'facturas.factura'
    _description = 'Factura'

    partner_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required=True
    )

    date = fields.Date(
        string='Fecha',
        required=True,
        default=fields.Date.context_today
    )
