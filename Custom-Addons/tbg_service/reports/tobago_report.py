# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import models, fields, tools


class DifferedCheckHistory(models.Model):
    _name = "report.tobago.order"
    _description = "Tobago Order Analysis"
    _auto = False

    name = fields.Char(string="Label")
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('no', 'Nothing to Invoice')
    ], string='Invoice Status', store=True)
    partner_id = fields.Many2one('res.partner', string='Customer')
    partner_invoice_id = fields.Many2one('res.partner', string='Invoice Address')
    partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address')
    order_date = fields.Datetime(string="Date")
    tobago_person = fields.Many2one('res.users', string='Tobago Person')
    total_amount = fields.Float(string='Total')
    currency_id = fields.Many2one("res.currency", string="Currency")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('order', 'Tobago Order'),
        ('process', 'Processing'),
        ('done', 'Done'),
        ('return', 'Returned'),
        ('cancel', 'Cancelled'),
    ], string='Status')

    _order = 'name desc'

    def _select(self):
        select_str = """
             SELECT
                    (select 1 ) AS nbr,
                    t.id as id,
                    t.name as name,
                    t.invoice_status as invoice_status,
                    t.partner_id as partner_id,
                    t.partner_invoice_id as partner_invoice_id,
                    t.partner_shipping_id as partner_shipping_id,
                    t.order_date as order_date,
                    t.tobago_person as tobago_person,
                    t.total_amount as total_amount,
                    t.currency_id as currency_id,
                    t.state as state
        """
        return select_str

    def _group_by(self):
        group_by_str = """
                GROUP BY
                    t.id,
                    name,
                    invoice_status,
                    partner_id,
                    partner_invoice_id,
                    partner_shipping_id,
                    order_date,
                    tobago_person,
                    total_amount,
                    currency_id,
                    state
        """
        return group_by_str

    def init(self):
        tools.sql.drop_view_if_exists(self._cr, 'report_tobago_order')
        self._cr.execute("""
            CREATE view report_tobago_order as
              %s
              FROM tobago_order t
                %s
        """ % (self._select(), self._group_by()))
