import unittest
from core.patterns import validate_amka, validate_iban, validate_afm, validate_luhn

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # Valid Luhn for AMKA (Sum is 30)
        self.assertTrue(validate_amka("01018012342"))

    def test_valid_afm(self):
        # Valid Modulo 11 (Sum is 1004, remainder 3)
        self.assertTrue(validate_afm("123456783"))

    def test_valid_iban(self):
        # Valid Modulo 97 Greek IBAN
        self.assertTrue(validate_iban("GR6101101230000012345678901"))

    def test_valid_credit_card(self):
        # Valid Visa Luhn Check
        self.assertTrue(validate_luhn("4539148902132590"))

if __name__ == '__main__':
    unittest.main()
