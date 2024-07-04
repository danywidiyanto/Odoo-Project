# -*- coding: utf-8 -*-
# from odoo import http


# class Hashmicrowedor(http.Controller):
#     @http.route('/hashmicrowedor/hashmicrowedor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hashmicrowedor/hashmicrowedor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hashmicrowedor.listing', {
#             'root': '/hashmicrowedor/hashmicrowedor',
#             'objects': http.request.env['hashmicrowedor.hashmicrowedor'].search([]),
#         })

#     @http.route('/hashmicrowedor/hashmicrowedor/objects/<model("hashmicrowedor.hashmicrowedor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hashmicrowedor.object', {
#             'object': obj
#         })
