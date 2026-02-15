import unittest
from core.patterns import validate_amka, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # 01018012342 passes the Luhn check (Sum is exactly 30)
        self.assertTrue(validate_amka("01018012342"), "Should pass valid Luhn check")

    def test_valid_afm(self):
        # 123456783 is valid: (Sum of weights is 1004. 1004 % 11 = 3)
        self.assertTrue(validate_afm("123456783"), "Should pass Modulo 11 check")

    def test_valid_iban(self):
        # GR61... is a mathematically valid Greek IBAN structure for these digits
        valid_gr_iban = "GR6101101230000012345678901"
        self.assertTrue(validate_iban(valid_gr_iban), "Should pass Modulo 97 validation")

if __name__ == '__main__':
    unittest.main()
