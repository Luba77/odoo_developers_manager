{
    'name': 'developers_management',
    'version': '1.0',
    'summary': 'Manage developers and their information',
    'description': """
        This module allows users to manage developers and their information.
        Users can create, edit, and view developers' profiles, including their
        names, contact details, types, addresses, and dates of birth.
    """,
    'author': 'Liubov Rudnevsla',
    'website': 'www.manage_developers.com',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'data': [
        'views/developer_tree_view.xml',
        'views/developers_template.xml',
        'views/company_tree_view.xml',
        'views/developer_form.xml',
        'views/company_form.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
