import unittest
from core.patterns import validate_afm

class TestAFMValidation(unittest.TestCase):

    def test_valid_afm(self):
        # έγκυρο ΑΦΜ 
        self.assertTrue(validate_afm("090000045"))

    def test_invalid_afm(self):
        # Ένα ΑΦΜ με λάθος τελευταίο ψηφίο
        self.assertFalse(validate_afm("123456780"))

    def test_short_afm(self):
        # ΑΦΜ με λιγότερα ψηφία
        self.assertFalse(validate_afm("12345"))

    def test_non_digit_afm(self):
        # ΑΦΜ με γράμματα
        self.assertFalse(validate_afm("12345678A"))

if __name__ == '__main__':
    unittest.main()