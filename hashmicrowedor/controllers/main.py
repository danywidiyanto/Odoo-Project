from odoo import http
from odoo.http import request

class Hasmicrowedor(http.Controller):
    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('hashmicrowedor.homepage_view')
