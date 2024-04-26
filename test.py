from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestDeveloperModel(TransactionCase):
    def test_create_developer(self):
        # Create a developer record
        developer = self.env['developers_management.developer'].create({
            'name': 'John Doe',
            'type': 'backend',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'address': '123 Main St, Anytown',
            'birthdate': '1990-01-01',
            'position': 'Developer',
        })

        # Check if the developer record is created correctly
        self.assertEqual(developer.name, 'John Doe')
        self.assertEqual(developer.type, 'backend')
        self.assertEqual(developer.phone, '123456789')
        self.assertEqual(developer.email, 'john.doe@example.com')
        self.assertEqual(developer.address, '123 Main St, Anytown')
        self.assertEqual(developer.birthdate, '1990-01-01')
        self.assertEqual(developer.position, 'Developer')

    def test_create_developer_without_name(self):
        # Attempt to create a developer record without a name
        with self.assertRaises(ValidationError):
            self.env['developers_management.developer'].create({
                'type': 'backend',
                'phone': '123456789',
                'email': 'john.doe@example.com',
                'address': '123 Main St, Anytown',
                'birthdate': '1990-01-01',
                'position': 'Developer',
            })
