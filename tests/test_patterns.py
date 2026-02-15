import unittest
from core.patterns import validate_amka, validate_iban, validate_afm

class TestValidationLogic(unittest.TestCase):

    def test_valid_amka(self):
        # 01018012342 passes the Luhn check (Sum is 30)
        self.assertTrue(validate_amka("01018012342"))

    def test_valid_iban(self):
        # A real, mathematically valid Greek IBAN structure
        self.assertTrue(validate_iban("GR1401101230000012345678901"))

    def test_valid_afm(self):
        # Sum of 12345677 is 1002. 1002 % 11 = 1. Final digit matches 1.
        self.assertTrue(validate_afm("123456771"))

if __name__ == '__main__':
    unittest.main()
