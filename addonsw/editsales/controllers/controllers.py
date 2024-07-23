# -*- coding: utf-8 -*-
# from odoo import http


# class Saleorder(http.Controller):
#     @http.route('/saleorder/saleorder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saleorder/saleorder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saleorder.listing', {
#             'root': '/saleorder/saleorder',
#             'objects': http.request.env['saleorder.saleorder'].search([]),
#         })

#     @http.route('/saleorder/saleorder/objects/<model("saleorder.saleorder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saleorder.object', {
#             'object': obj
#         })
