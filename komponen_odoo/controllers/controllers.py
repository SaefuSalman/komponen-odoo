# -*- coding: utf-8 -*-
# from odoo import http


# class KomponenOdoo(http.Controller):
#     @http.route('/komponen_odoo/komponen_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/komponen_odoo/komponen_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('komponen_odoo.listing', {
#             'root': '/komponen_odoo/komponen_odoo',
#             'objects': http.request.env['komponen_odoo.komponen_odoo'].search([]),
#         })

#     @http.route('/komponen_odoo/komponen_odoo/objects/<model("komponen_odoo.komponen_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('komponen_odoo.object', {
#             'object': obj
#         })
