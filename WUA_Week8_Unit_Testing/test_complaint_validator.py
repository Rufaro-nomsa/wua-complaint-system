import unittest
from complaint_validator import validate_complaint


class TestComplaintValidator(unittest.TestCase):

    def test_valid_complaint(self):
        self.assertTrue(validate_complaint("Broken classroom equipment"))

    def test_empty_complaint(self):
        self.assertFalse(validate_complaint(""))

    def test_spaces_only(self):
        self.assertFalse(validate_complaint("   "))

    def test_another_valid_complaint(self):
        self.assertTrue(validate_complaint("Water supply problem"))


if __name__ == "__main__":
    unittest.main()