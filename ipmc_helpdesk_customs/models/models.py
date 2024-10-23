# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ipmc_helpdesk_customs(models.Model):
#     _name = 'ipmc_helpdesk_customs.ipmc_helpdesk_customs'
#     _description = 'ipmc_helpdesk_customs.ipmc_helpdesk_customs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
