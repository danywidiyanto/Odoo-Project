# -*- coding: utf-8 -*-
# from odoo import http


# class Sekolahcons(http.Controller):
#     @http.route('/sekolahcons/sekolahcons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sekolahcons/sekolahcons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sekolahcons.listing', {
#             'root': '/sekolahcons/sekolahcons',
#             'objects': http.request.env['sekolahcons.sekolahcons'].search([]),
#         })

#     @http.route('/sekolahcons/sekolahcons/objects/<model("sekolahcons.sekolahcons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sekolahcons.object', {
#             'object': obj
#         })
