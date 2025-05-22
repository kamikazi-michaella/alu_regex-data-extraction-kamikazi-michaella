import unittest
from regex_validation import validate_email, validate_phone, validate_url, validate_credit_card

class TestRegexValidation(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertFalse(validate_email("invalid-email.com"))

    def test_validate_phone(self):
        self.assertTrue(validate_phone("(123) 456-7890"))
        self.assertFalse(validate_phone("12345"))

    def test_validate_url(self):
        self.assertTrue(validate_url("https://www.example.com"))
        self.assertFalse(validate_url("htp://invalid-url"))

    def test_validate_credit_card(self):
        self.assertTrue(validate_credit_card("1234 5678 9012 3456"))
        self.assertFalse(validate_credit_card("123456789012345"))

if __name__ == '__main__':
    unittest.main()
