# -*- coding: utf-8 -*-
# from odoo import http


# class Apideco(http.Controller):
#     @http.route('/apideco/apideco', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apideco/apideco/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('apideco.listing', {
#             'root': '/apideco/apideco',
#             'objects': http.request.env['apideco.apideco'].search([]),
#         })

#     @http.route('/apideco/apideco/objects/<model("apideco.apideco"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apideco.object', {
#             'object': obj
#         })
