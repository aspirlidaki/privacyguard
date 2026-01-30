import unittest
from core.patterns import validate_afm

class TestAFMValidation(unittest.TestCase):
    """
    Unit Tests για την επαλήθευση της λογικής του Modulo 11
    valid, invalid και edge cases.
    """

    def test_valid_afm_scenarios(self):
        """Έλεγχος γνωστών έγκυρων ΑΦΜ (Happy Path)."""
        # Λίστα με πραγματικά/έγκυρα ΑΦΜ για μαζικό έλεγχο
        valid_afms = [
           "090000045",  # Κλασικό έγκυρο
            "123456783",  # Μαθηματικά έγκυρο 
            "731388439"   # Τυχαίο έγκυρο
        ]
        
        for afm in valid_afms:
            with self.subTest(afm=afm):
                self.assertTrue(validate_afm(afm), f"Failed valid AFM: {afm}")

def test_mathematically_invalid_afm(self):
        """ΑΦΜ που έχουν 9 ψηφία, αλλά αποτυγχάνουν στον τύπο."""
        invalid_afms = [
            "123456789", # Τυχαία σειρά
            "000000000", # Μηδενικά (πλέον κόβεται από τον κώδικα)
            "111111111"  # Ίδια ψηφία
        ]
        for afm in invalid_afms:
            with self.subTest(afm=afm):
                self.assertFalse(validate_afm(afm), f"Should fail math check: {afm}")

def test_invalid_length(self):
        """Boundary Testing: Έλεγχος μήκους."""
        self.assertFalse(validate_afm("12345678"), "Should fail (8 digits)")
        self.assertFalse(validate_afm("1234567890"), "Should fail (10 digits)")
        self.assertFalse(validate_afm(""), "Should fail (empty string)")

def test_invalid_characters(self):
        """Input Validation: Έλεγχος χαρακτήρων."""
        self.assertFalse(validate_afm("12345678A"), "Should fail (letter)")
        self.assertFalse(validate_afm("12-345678"), "Should fail (symbol)")

if __name__ == '__main__':
    unittest.main()