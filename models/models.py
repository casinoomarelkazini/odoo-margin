# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class set_price_from_marrgin(models.Model):
#     _name = 'set_price_from_marrgin.set_price_from_marrgin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100