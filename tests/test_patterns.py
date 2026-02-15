import unittest
from core.patterns import validate_amka, validate_iban, validate_afm, validate_luhn

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # Valid Luhn: 01018012342 (Sum is 30)
        self.assertTrue(validate_amka("01018012342"))

    def test_valid_afm(self):
        # Valid Modulo 11: 123456783 (Sum is 1004, Remainder is 3)
        self.assertTrue(validate_afm("123456783"))

    def test_valid_iban(self):
        # Valid Greek IBAN for Modulo 97 check
        self.assertTrue(validate_iban("GR6101101230000012345678901"))

    def test_valid_credit_card(self):
        # Valid Visa number for Luhn check
        self.assertTrue(validate_luhn("4539148902132595"))

if __name__ == '__main__':
    unittest.main()
