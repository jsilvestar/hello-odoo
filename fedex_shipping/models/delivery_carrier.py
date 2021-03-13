# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"


    delivery_type = fields.Selection(selection_add=[('fedex', 'Fedex')])
    account_no = fields.Char('Account No')
    meter_no = fields.Char('Meter No')
    integration_id = fields.Char('Integration ID')
    fedex_key = fields.Char('Fedex Key')
    fedex_password = fields.Char('Fedex Password')






