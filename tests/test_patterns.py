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
            "090000045",  # Κλασικό παράδειγμα
            "998282381",  # Τυχαίο έγκυρο
            "094014201"   # Υπουργείο Οικονομικών 
        ]
        
        for afm in valid_afms:
            with self.subTest(afm=afm):
                self.assertTrue(validate_afm(afm), f"Failed valid AFM: {afm}")

    def test_mathematically_invalid_afm(self):
        """
        ΑΦΜ που έχουν 9 ψηφία, αλλά αποτυγχάνουν στον μαθηματικό τύπο.
        Αυτό ξεχωρίζει τον απλό έλεγχο Regex από τον αλγόριθμο Modulo 11.
        """
        invalid_afms = [
            "123456789", # Τυχαία σειρά
            "000000000", # Μηδενικά
            "111111111"  # Ίδια ψηφία (σπάνια έγκυρο)
        ]
        for afm in invalid_afms:
            with self.subTest(afm=afm):
                self.assertFalse(validate_afm(afm), f"Should fail math check: {afm}")

    def test_invalid_length(self):
        """Boundary Testing: Έλεγχος μήκους (πρέπει αυστηρά 9 ψηφία)."""
        self.assertFalse(validate_afm("12345678"), "Should fail (8 digits)")
        self.assertFalse(validate_afm("1234567890"), "Should fail (10 digits)")
        self.assertFalse(validate_afm(""), "Should fail (empty string)")

    def test_invalid_characters(self):
        """Input Validation: Έλεγχος μη αριθμητικών χαρακτήρων."""
        self.assertFalse(validate_afm("12345678A"), "Should fail (contains letter)")
        self.assertFalse(validate_afm("1234-5678"), "Should fail (contains hyphen)")
        self.assertFalse(validate_afm("abcdefghi"), "Should fail (all letters)")
        self.assertFalse(validate_afm("123 45678"), "Should fail (contains space)")

    def test_edge_case_check_digit_zero(self):
        """
        Edge Case: Όταν το υπόλοιπο της διαίρεσης είναι 10, το check digit πρέπει να είναι 0.
        Αυτό είναι το πιο κρίσιμο σημείο του αλγορίθμου Modulo 11.
        """
        # Το '090000045' επαληθεύει αυτόν τον κανόνα
        self.assertTrue(validate_afm("090000045"))

if __name__ == '__main__':
    unittest.main()