from odoo import models, fields

class LoginRedirectConfig(models.Model):
    _name = 'login.redirect.config'
    _description = 'Login Redirect Configuration'
    _order = 'name'

    name = fields.Char(string='Configuration Name', required=True)
    username = fields.Char(
        string='Username',
        required=True,
        help='The username to match for redirect'
    )
    password = fields.Char(
        string='Password',
        required=True,
        help='The password to match for redirect'
    )
    redirect_url = fields.Char(
        string='Redirect URL',
        required=True,
        help='The URL to redirect to (e.g., /web/app/sales or https://example.com)'
    )
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Enable or disable this redirect rule'
    )
