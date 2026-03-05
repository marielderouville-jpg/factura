from odoo import models, fields


class FacturaLinea(models.Model):
    _name = 'facturas.factura.linea'
    _description = 'Línea de Factura'

    factura_id = fields.Many2one(
        'facturas.factura',
        string='Factura',
        ondelete='cascade',
        required=True
    )

    product_id = fields.Many2one(
        'product.product',
        string='Producto',
        required=True
    )

    quantity = fields.Float(
        string='Cantidad',
        default=1.0,
        required=True
    )

    price_unit = fields.Float(
        string='Precio',
        required=True
    )
