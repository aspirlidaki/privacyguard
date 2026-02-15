import unittest
from core.patterns import validate_luhn, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_afm(self):
        # Valid: Sum weighted by powers of 2 results in check digit 3
        self.assertTrue(validate_afm("123456783"), "Should pass Modulo 11 check")

    def test_valid_iban(self):
        # Valid Greek IBAN that passes Modulo 97 check
        self.assertTrue(validate_iban("GR6101101230000012345678901"), "Should pass Modulo 97 validation")

    def test_valid_credit_card(self):
        # Correctly formatted Visa passing Luhn check
        self.assertTrue(validate_luhn("4539148802132590"), "Should pass Luhn check")

    def test_valid_amka(self):
        # Valid Luhn for AMKA
        self.assertTrue(validate_luhn("01018012342"), "Should pass Luhn check")

if __name__ == '__main__':
    unittest.main()
