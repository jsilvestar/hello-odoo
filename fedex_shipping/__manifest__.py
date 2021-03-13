# -*- coding: utf-8 -*-
{
    'name' : 'Fedex Delivery',
    'version' : '1.0',
    'summary': 'Fedex Delivery',
    'sequence': 15,
    'description': """
Fedex Delivery
    """,
    'category': 'Delivery',
    'depends' : ['delivery', 'product'],
    'data': [
        'views/delivery_carrier_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
