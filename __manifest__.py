

{
    'name': "amend-fields",
    'author': "amend-fields",
    'category': 'purchase',
    'summary': """amend-fields""",
    'website': 'http://www.asceticbs.com',
    'license': 'AGPL-3',
    'description': """amend-fields""",
    'version': '14.0.1.0',
    'depends': ['stock', ],
    "data": [
        "views/view_picking_form.xml",
        "views/stock_picking_move_tree.xml",
        "views/stock_picking_tree.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
