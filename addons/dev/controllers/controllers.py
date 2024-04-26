from odoo import http
from odoo.http import request

class DeveloperController(http.Controller):
    @http.route('/developers', auth='user', csrf=False, website=True)
    def developers_page(self):
        """
            Developer's menu
        """
        return http.request.render('dev.developers_management_developers_template')

    @http.route('/developer/search', type='http',  auth='user', csrf=False, website=True)
    def developer_filter(self, name=None, type=None, phone=None):
        """
            Developer's filter
        """
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

    @http.route('/company/search', type='http',  auth='user', csrf=False,  website=True)
    def company_filter(self, name=None):
        """
            Company's filter
        """
        domain = []
        if name:
            domain += [('name', 'ilike', name)]
        companies = request.env['developers_management.company'].search(domain)

        return http.request.render('dev.developers_management_companies_tree_view_template', {
            'companies': companies,
        })

    @http.route('/view_developers', type='http',  auth='user', csrf=False, website=True)
    def developer_tree_view(self):
        """
            View developers
        """
        developers = request.env['developers_management.developer'].sudo().search([])
        return http.request.render('dev.developers_management_tree_view_template', {'developers': developers})

    @http.route('/view_companies', type='http',  auth='user', csrf=False, website=True)
    def company_tree_view(self):
        """
            View companies
        """
        companies = request.env['developers_management.company'].sudo().search([])
        return http.request.render('dev.developers_management_companies_tree_view_template', {'companies': companies})

    @http.route('/developers/new', type='http', auth='user', csrf=False, website=True)
    def developer_form(self):
        """
            Create developer form
        """
        companies = request.env['developers_management.company'].search([])
        developers = request.env['developers_management.developer'].sudo().search([])
        return http.request.render('dev.developers_management_developer_form', {
            'companies': companies,
            'developers': developers,
        })


    @http.route('/developers/create', type='http', auth='user', csrf=False, website=True)
    def create_developer(self, **post):
        """
            Create developer view
        """
        developer = request.env['developers_management.developer']
        developer.create({
            'name': post.get('name'),
            'type': post.get('type'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'address': post.get('address'),
            'birthdate': post.get('birthdate'),
            'position': post.get('position'),
            'company_id': post.get('company_id'),
        })
        return http.request.redirect('/view_developers')

    @http.route('/companies/new', auth='public', csrf=False, website=True)
    def company_form(self):
        """
            Create company form
        """
        developers = request.env['developers_management.developer'].search([])
        return http.request.render('dev.developers_management_company_form', {
            'developers': developers,
        })

    @http.route('/companies/create', type='http', auth='public', website=True, csrf=False)
    def create_company(self, **post):
        """
           Create company view
        """
        company = request.env['developers_management.company'].sudo().create({
            'name': post.get('name'),
            'address': post.get('address'),
        })

        developer_ids = request.httprequest.form.getlist('developer_ids')
        developer_ids = [int(developer_id) for developer_id in developer_ids]
        company.developers = [(4, developer_id, 0) for developer_id in developer_ids]
        return http.request.redirect('/view_companies')
