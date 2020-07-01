from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        email="test@abc.com"
        password="Testpass123"
        user= get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_check_normalize_email_address(self):
        email="test@ABCF.cOm"
        user=get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email, email.lower())

    def test_valid_email_address(self):
        """test creating user with no email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_super_user_Creation(self):
        user=get_user_model().objects.create_superuser(
            'adtest@abcf.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        