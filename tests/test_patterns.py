import unittest
from core.patterns import validate_amka, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # Luhn check: 01018012342
        self.assertTrue(validate_amka("01018012342"))

    def test_valid_iban(self):
        # A known valid Greek IBAN structure
        self.assertTrue(validate_iban("GR1401101230000012345678901"))

    def test_valid_afm(self):
        # AFM where Sum % 11 matches the check digit
        # Example: 123456781 (Sum=1112, Remainder=1)
        self.assertTrue(validate_afm("123456781"), "Should pass Modulo 11 check")

if __name__ == '__main__':
    unittest.main()
    
