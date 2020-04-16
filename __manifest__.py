# -*- coding: utf-8 -*-
{
    'name': "express_shipping",

    'summary': """
        Adds express shipping checkbox. """,

    'description': """
        Adds express shipping checkbox, and calculates it if You have two 
        or more order lines and a checkbox, module creates two deliveries.
    """,

    'author': "AlexJack",
    'website': "https://alexvjack.github.io/",

    'category': 'Uncategorized',
    'version': '13.0.0.1.0',

    'depends': [
        'base',
        'sale',
    ],

    'data': [
        'views/views.xml',
    ],
}
