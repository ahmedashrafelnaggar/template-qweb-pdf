# -*- coding: utf-8 -*-
# from odoo import http


# class IpmcHelpdeskCustoms(http.Controller):
#     @http.route('/ipmc_helpdesk_customs/ipmc_helpdesk_customs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipmc_helpdesk_customs/ipmc_helpdesk_customs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipmc_helpdesk_customs.listing', {
#             'root': '/ipmc_helpdesk_customs/ipmc_helpdesk_customs',
#             'objects': http.request.env['ipmc_helpdesk_customs.ipmc_helpdesk_customs'].search([]),
#         })

#     @http.route('/ipmc_helpdesk_customs/ipmc_helpdesk_customs/objects/<model("ipmc_helpdesk_customs.ipmc_helpdesk_customs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipmc_helpdesk_customs.object', {
#             'object': obj
#         })
