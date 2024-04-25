from odoo import models, fields


class Company(models.Model):
    _name = 'developers_management.company'
    _description = 'Company'

    name = fields.Char(required=True)
    address = fields.Text()
    developers = fields.One2many('developers_management.developer',
                                    'company_id', string='Developers')