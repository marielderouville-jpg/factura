{
    'name': 'Facturas Simples',
    'version': '1.0',
    'summary': 'Módulo básico para crear facturas de clientes',
    'description': 'Permite crear facturas con cliente, fecha y líneas de productos.',
    'category': 'Accounting',
    'author': 'Tu Nombre',
    'depends': [
        'base',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/factura_views.xml',
    ],
    'installable': True,
    'application': True,
}
