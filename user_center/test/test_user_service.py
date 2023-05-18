import unittest
from user_center.app import app
from user_center.user_center.Models.models import User, db
from user_center.app import create_user

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app_context('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        # Assume create_user function takes two arguments: username and email
        create_user('testuser', 'testuser@example.com')
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testuser@example.com')

if __name__ == '__main__':
    unittest.main()
