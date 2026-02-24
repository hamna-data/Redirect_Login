import logging
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from werkzeug.wrappers import Response

_logger = logging.getLogger(__name__)


class LoginRedirectController(http.Controller):
    """Custom login redirect controller."""

    @http.route('/web/login', type='http', auth='none', priority=100)
    def web_login(self, redirect=None, **kw):
        """
        Override web login to redirect specific users.
        Priority 100 ensures this runs before default handlers.
        """
        _logger.info("=== LOGIN REDIRECT: web_login called")
        
        if request.httprequest.method == 'POST':
            login = kw.get('login', '')
            password = kw.get('password', '')
            
            _logger.info(f"=== LOGIN REDIRECT: POST attempt - login={login}")
            
            if login and password:
                try:
                    # Check for redirect config FIRST
                    redirect_configs = request.env['login.redirect.config'].sudo().search([
                        ('active', '=', True),
                        ('username', '=', login),
                        ('password', '=', password),
                    ], limit=1)
                    
                    _logger.info(f"=== LOGIN REDIRECT: Found {len(redirect_configs)} configs")
                    
                    if redirect_configs:
                        redirect_url = redirect_configs[0].redirect_url
                        _logger.info(f"=== LOGIN REDIRECT: Config match! URL={redirect_url}")
                        
                        # For redirect users, call home login to authenticate
                        home_controller = Home()
                        home_controller.web_login(redirect='/web', **kw)
                        
                        # Now return a clean redirect response
                        _logger.info(f"=== LOGIN REDIRECT: Redirecting to {redirect_url}")
                        return Response('Redirecting...', status=302, headers={'Location': redirect_url})
                except Exception as e:
                    _logger.error(f"=== LOGIN REDIRECT: Exception - {str(e)}", exc_info=True)
        
        # For GET requests or non-matching logins, use default Home controller
        _logger.info("=== LOGIN REDIRECT: Using default login handler")
        home_controller = Home()
        return home_controller.web_login(redirect=redirect, **kw)
