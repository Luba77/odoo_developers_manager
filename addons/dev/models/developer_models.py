from odoo import models, fields, api


class Developer(models.Model):
    _name = 'developers_management.developer'
    _description = 'Developer'

    name = fields.Char(string='Name', required=True)
    type = fields.Selection([
        ('front-end', 'Front-end'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out Stuff'),
    ], string='Type', required=False)
    global_identification = fields.Char(compute='_compute_global_identification', string='Global Identification', store=True)
    phone = fields.Char(string='Phone', domain="[('type', '!=', 'out-stuff')]")
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    birthdate = fields.Date(string='Birthdate')
    position = fields.Char()
    company_id = fields.Many2one('developers_management.company')

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = \
                f'{developer.name}-{developer.type}'



