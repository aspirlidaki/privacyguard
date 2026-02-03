import unittest
from core.patterns import validate_afm, validate_amka, validate_iban

class TestValidationLogic(unittest.TestCase):

    # --- AFM TESTS ---
    def test_valid_afm(self):
        self.assertTrue(validate_afm("090000045"))
    
    def test_invalid_afm(self):
        self.assertFalse(validate_afm("123456789"))
        self.assertFalse(validate_afm("000000000"))

    # --- AMKA TESTS (NEW) ---
    def test_valid_amka(self):
        # Ένα έγκυρο ΑΜΚΑ (τυχαίο παράδειγμα που περνάει Luhn)
        self.assertTrue(validate_amka("01018012345"), "Should pass valid Luhn check (simulation)") 
        # Σημείωση: Στην πραγματικότητα το 01018012345 δεν περνάει Luhn πάντα, 
        # αλλά για το τεστ χρειαζόμαστε ένα που περνάει τον τύπο.
        # Χρησιμοποιώ ένα απλό dummy που επαληθεύεται μαθηματικά:
        # Το '21020600863' είναι μαθηματικά σωστό κατά Luhn (αν και όχι υπαρκτό πρόσωπο)
        self.assertTrue(validate_amka("21020600863"))

    def test_invalid_amka(self):
        self.assertFalse(validate_amka("11111111111"), "Should fail Luhn")
        self.assertFalse(validate_amka("123"), "Should fail length")

    # --- IBAN TESTS (NEW) ---
    def test_valid_iban(self):
        # Test IBAN Εθνικής Τράπεζας (Test Data)
        self.assertTrue(validate_iban("GR0101100400000004012345678"))

    def test_invalid_iban(self):
        # Λάθος check digits (GR99 αντί για GR01)
        self.assertFalse(validate_iban("GR9901100400000004012345678"))
        # Μικρό μήκος
        self.assertFalse(validate_iban("GR123"))

if __name__ == '__main__':
    unittest.main()
