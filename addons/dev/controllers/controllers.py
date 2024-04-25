from odoo import http
from odoo.http import request

class DeveloperController(http.Controller):

    @http.route('/developer/search', type='http', auth='public', website=True)
    def developer_filter(self, name=None, type=None, phone=None, **kwargs):
        domain = []
        if name:
            domain += [('name', 'ilike', name)]
        if phone:
            domain += [('phone', 'ilike', phone)]
        if type:
            domain += [('type', '=', type)]

        developers = request.env['developers_management.developer'].search(domain)

        return http.request.render('dev.developers_management_tree_view_template', {
            'developers': developers,
        })

    @http.route('/developers', auth='public', csrf=False, website=True)
    def developer_tree_view(self, **kwargs):
        developers = request.env['developers_management.developer'].sudo().search([])
        return http.request.render('dev.developers_management_tree_view_template', {'developers': developers})
