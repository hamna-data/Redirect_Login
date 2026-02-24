{
    'name': 'Login Redirect',
    'category': 'Tools',
    'summary': 'Redirect specific users to a custom URL after login',
    'description': '''
        This module redirects specific users to a custom URL after login.
        Supports both app URLs and external URLs with timestamp parameters.
    ''',
    'author': 'Hamna Sakhawat',
    'website': 'https://www.example.com',
    'depends': ['web', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/login_redirect_config.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
