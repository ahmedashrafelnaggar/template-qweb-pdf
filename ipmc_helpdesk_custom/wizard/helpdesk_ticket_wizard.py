from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HelpdeskTicketWizard(models.TransientModel):
    _name = 'helpdesk.ticket.wizard'
    _description = ' Helpdesk Wizard'

    outgoing = fields.Boolean(string="صادرة")
    incoming = fields.Boolean(string="واردة")
    transaction_tpe = fields.Selection([
        ('incoming', 'Incoming'),
        ('outgoing', 'Outgoing')
    ], string='Transaction Type')

    stage_id = fields.Many2one(
        'helpdesk.stage',
    )
    date_from = fields.Date(string="التاريخ من")
    date_to = fields.Date(string="التاريخ إلى")

    partner_ids = fields.Many2many('res.partner', string="الجهة", required=True)
    oolweh_mualamah_priority = fields.Selection([
        ('عاجل', 'عاجل'),
        ('عاجل جدا وهام', 'عاجل جدا وهام'),
        ('عاجل جدا وهام يسلم حالا', 'عاجل جدا وهام يسلم حالا'),
        ('سري', 'سري'),
        ('سري-عاجل جدا وهام', 'سري-عاجل جدا وهام'),
        ('يفتح بيد سعادته', 'يفتح بيد سعادته'),
    ], string='أولوية المعاملة', required=True)

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for record in self:
            if record.date_from and record.date_to:
                if record.date_from > record.date_to:
                    raise ValidationError("تاريخ البدء يجب أن يكون قبل تاريخ الانتهاء.")
    def print_pdf(self):
        pass

    def print_xlsx(self):
        pass