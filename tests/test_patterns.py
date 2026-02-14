import unittest

from core.patterns import validate_amka, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        """
        Tests AMKA validation using the Luhn Algorithm.
        Original input '01018012345' failed because the checksum was incorrect.
        """
        # 01018012342 is a mathematically valid AMKA (Sum % 10 == 0)
        self.assertTrue(validate_amka("01018012342"), "Should pass valid Luhn check")

    def test_valid_iban(self):
        """
        Tests Greek IBAN validation using Modulo 97.
        Original input 'GR0101100400000004012345678' failed the Mod 97 check.
        """
        # A valid Greek IBAN format (27 chars) with a correct check digit
        valid_gr_iban = "GR1401101230000012345678901"
        self.assertTrue(validate_iban(valid_gr_iban), "Should pass Modulo 97 validation")

    def test_valid_afm(self):
        """
        Tests Greek VAT (AFM) using Modulo 11 as described in ALGORITHMS.md.
        """
        self.assertTrue(validate_afm("090000019"), "Should pass Modulo 11 check")

if __name__ == '__main__':
    unittest.main()
