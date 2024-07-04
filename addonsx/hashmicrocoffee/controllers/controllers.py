# -*- coding: utf-8 -*-
# from odoo import http


# class Hashmicrocoffee(http.Controller):
#     @http.route('/hashmicrocoffee/hashmicrocoffee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hashmicrocoffee/hashmicrocoffee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hashmicrocoffee.listing', {
#             'root': '/hashmicrocoffee/hashmicrocoffee',
#             'objects': http.request.env['hashmicrocoffee.hashmicrocoffee'].search([]),
#         })

#     @http.route('/hashmicrocoffee/hashmicrocoffee/objects/<model("hashmicrocoffee.hashmicrocoffee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hashmicrocoffee.object', {
#             'object': obj
#         })
