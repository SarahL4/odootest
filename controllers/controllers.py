# -*- coding: utf-8 -*-
from odoo import http

# class SarahModule(http.Controller):
#     @http.route('/sarah_module/sarah_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sarah_module/sarah_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sarah_module.listing', {
#             'root': '/sarah_module/sarah_module',
#             'objects': http.request.env['sarah_module.sarah_module'].search([]),
#         })

#     @http.route('/sarah_module/sarah_module/objects/<model("sarah_module.sarah_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sarah_module.object', {
#             'object': obj
#         })