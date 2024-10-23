from odoo import api, fields, models
from datetime import datetime
from hijri_converter import Gregorian, Hijri
from hijri_converter import convert

class helpdesk_ticket(models.Model):
    _inherit = 'helpdesk.ticket'
    _description = "Helpdesk ticket"

    sub_customer = fields.Many2many(
        'res.partner',
        string="Sub Customers",
        relation="helpdesk_ticket_res_partner_rel",
        column1="ticket_id",
        column2="partner_id"
    )


    hijri_date = fields.Char(string='Hijiri Date')
    hijri_year = fields.Char(string="Hijri Year", compute="_compute_hijri_year", store=1)

    def action_print_reports(self):
        if self.outgoing:
            return self.env.ref('ipmc_helpdesk_customs.outgoing_report_id').report_action(self)
        else:
            return self.env.ref('ipmc_helpdesk_customs.incoming_report_id').report_action(self)


    @api.onchange('transaction_date')
    def _onchange_hijri_date(self):
        if self.transaction_date:
            # Convert Gregorian to Hijri
            hijri_date = convert.Gregorian(self.transaction_date.year,
                                           self.transaction_date.month,self.transaction_date.day).to_hijri()
            hijri_month_names = [
                'محرم', 'صفر', 'ربيع الأول', ' ربيع الثاني',
                'جمادي الأول', 'جمادي الثاني', 'رجب', 'شعبان',
                'رمضان', 'شوال', ' ذو القعدة', 'ذو الحجة'
            ]
            hijri_month_name = hijri_month_names[hijri_date.month - 1]
            self.hijri_date = f" {hijri_date.year}-{hijri_month_name}-{hijri_date.day} "
    @api.depends('hijri_date')
    def _compute_hijri_year(self):
        for record in self:
            # Assuming 'hijri_date' is in the format "YYYY-MMM-DD"
            if record.hijri_date:
                # Split by the hyphen and extract the first part, which is the year
                hijri_year = record.hijri_date.split('-')[0]
                record.hijri_year = hijri_year