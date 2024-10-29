from odoo import api, fields, models
from datetime import datetime
from hijri_converter import Gregorian, Hijri
from hijri_converter import convert
from hijri_converter import convert  # تأكد من تثبيت المكتبة hijri-converter


class helpdesk_ticket(models.Model):
    _inherit = 'helpdesk.ticket'
    _description = "Helpdesk ticket"

    sub_customer = fields.Many2many('res.partner',string="Sub Customers")
    transaction_date = fields.Date(string="Transaction Date")
    hijri_date = fields.Char(string='Hijiri Date')
    hijri_year = fields.Char(string="Hijri Year", compute="_compute_hijri_year")
    # hijri_year = fields.Integer(string='Hijri Year', compute='_compute_hijri_year', store=True)

    def action_print_reports(self):
        if self.outgoing:
            return self.env.ref('ipmc_helpdesk_customs.outgoing_report_id').report_action(self)
        else:
            return self.env.ref('ipmc_helpdesk_customs.incoming_report_id').report_action(self)



    # @api.depends('hijri_date')
    # def _compute_hijri_year(self):
    #     for ticket in self:
    #         if ticket.hijri_date:
    #             # قم بإضافة منطق تحويل التاريخ الهجري إلى السنة هنا
    #             hijri_date = fields.Date.from_string(ticket.hijri_date)
    #             # مثال بسيط، يمكنك استخدام مكتبة hijri_converter للحصول على السنة الصحيحة
    #             ticket.hijri_year = hijri_date.year  # استبدل هذا بالمنطق الصحيح
    #         else:
    #             ticket.hijri_year = 0

    @api.depends('hijri_date')
    def _compute_hijri_year(self):
        for record in self:
            # Assuming 'hijri_date' is in the format "YYYY-MMM-DD"
            if record.hijri_date:
                # Split by the hyphen and extract the first part, which is the year
                hijri_year = record.hijri_date.split('-')[0]
                record.hijri_year = hijri_year

    @api.model
    def convert_transaction_date_to_hijri(self):
        records = self.search([('hijri_date', '=', False)])
        print("records:", records)
        if not records:
            return "No records found."

        for record in records:
            if record.transaction_date:
                hijri_date = convert.Gregorian(
                    record.transaction_date.year,
                    record.transaction_date.month,
                    record.transaction_date.day
                ).to_hijri()

                # Step 3: التحقق من التحويل
                if not hijri_date:
                    return "No records converted."

                hijri_month_names = [
                    'محرم', 'صفر', 'ربيع الأول', 'ربيع الثاني', 'جمادى الأولى',
                    'جمادى الآخرة', 'رجب', 'شعبان', 'رمضان', 'شوال',
                    'ذو القعدة', 'ذو الحجة'
                ]
                hijri_month_name = hijri_month_names[hijri_date.month - 1]
                record.hijri_date = f"{hijri_date.year}-{hijri_month_name}-{hijri_date.day}"


