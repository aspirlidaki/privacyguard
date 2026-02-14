import unittest
from core.patterns import validate_amka, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # Luhn check: 01018012342 (Sum=30, 30%10=0)
        self.assertTrue(validate_amka("01018012342"))

    def test_valid_iban(self):
        # Known valid Greek IBAN structure
        self.assertTrue(validate_iban("GR1401101230000012345678901"))

    def test_valid_afm(self):
        """
        Tests Greek VAT (AFM) using Modulo 11 logic.
        """
        # Sum of 12345677 is 1002. 1002 % 11 = 1.
        self.assertTrue(validate_afm("123456771"), "Should pass Modulo 11 check")

if __name__ == '__main__':
    unittest.main()
    
