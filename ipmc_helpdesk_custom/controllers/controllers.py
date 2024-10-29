# -*- coding: utf-8 -*-
# from odoo import http


# class IpmcHelpdeskCustom(http.Controller):
#     @http.route('/ipmc_helpdesk_custom/ipmc_helpdesk_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipmc_helpdesk_custom/ipmc_helpdesk_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipmc_helpdesk_custom.listing', {
#             'root': '/ipmc_helpdesk_custom/ipmc_helpdesk_custom',
#             'objects': http.request.env['ipmc_helpdesk_custom.ipmc_helpdesk_custom'].search([]),
#         })

#     @http.route('/ipmc_helpdesk_custom/ipmc_helpdesk_custom/objects/<model("ipmc_helpdesk_custom.ipmc_helpdesk_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipmc_helpdesk_custom.object', {
#             'object': obj
#         })
