# -*- coding: utf-8 -*-
# from odoo import http


# class Recordset(http.Controller):
#     @http.route('/recordset/recordset/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recordset/recordset/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recordset.listing', {
#             'root': '/recordset/recordset',
#             'objects': http.request.env['recordset.recordset'].search([]),
#         })

#     @http.route('/recordset/recordset/objects/<model("recordset.recordset"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recordset.object', {
#             'object': obj
#         })
