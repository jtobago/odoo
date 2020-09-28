# -*- coding: utf-8 -*-
{
    'name': "tbg_service",

    'summary': """Module developed by Juliano Kersting - Phoenix & Tobago.""",

    'description': """Este módulo foi criado para o gerenciamento de Serviços Phoenix & Tobago.        
    
            - Gerencia do processo do inicio ao fim
            - Afiações
            - Reparos
            - Garantias - em breve
            - Manutençao de equipamentos de afiação (Refaceamento) - em breve
            - Gerencia de Estoque e relacionamento com clientes""",

    'author': "Phoenix & Tobago",
    'website': "https://www.tobago.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'account'],
    'data': [
        'data/data.xml',
        'security/tobago_security.xml',
        'security/ir.model.access.csv',
        'views/tobago_view.xml',
        'views/repair_view.xml',
        'views/config_view.xml',
        'views/tobago_report.xml',
        'views/tobago_label.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}