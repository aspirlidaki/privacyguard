"""
PrivacyGuard Pro - Detection Patterns & Validation Logic
------------------------------------------------------
Author: Anastasia S.
Description: 
    Περιέχει τις υπογραφές (Signatures) για την ανίχνευση μυστικών και 
    τους μαθηματικούς αλγορίθμους επαλήθευσης (Validation).

Security Note: 
    Τα Regex είναι optimized για ακρίβεια και αποφυγή ReDoS (Regular Expression DoS).
"""

# --- 1. DETECTION SIGNATURES (REGEX) ---
PATTERNS = {
    # Google API Keys ξεκινούν πάντα με 'AIza' και έχουν 39 χαρακτήρες σύνολο
    'Google API Key': r'AIza[0-9A-Za-z-_]{35}',
    
    # AWS Access Keys ξεκινούν με 'AKIA' (Identity) και έχουν 20 χαρακτήρες
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    
    # GitHub Personal Access Tokens (Modern format starts with ghp_)
    'GitHub Token': r'ghp_[a-zA-Z0-9]{36}',
    
    # Ελληνικό ΑΦΜ: 9 ψηφία.
    # Χρησιμοποιούμε \b (word boundaries) για να ΜΗΝ πιάνω τηλέφωνα ή timestamps.
    'Greek AFM (VAT)': r'\b\d{9}\b',
}

# --- 2. VALIDATION ALGORITHMS ---

def validate_afm(afm: str) -> bool:
    """
    Εκτελεί μαθηματική επαλήθευση Ελληνικού ΑΦΜ βάσει του αλγορίθμου Modulo 11.
    
    Args:
        afm (str): Το 9ψήφιο string προς έλεγχο.
        
    Returns:
        bool: True αν είναι έγκυρο, False αν είναι τυχαία νούμερα.
    """
    # Fail Fast: Αν δεν είναι 9 ψηφία, απορρίπτεται αμέσως.
    if not afm.isdigit() or len(afm) != 9:
        return False
    
    try:
        # Μετατροπή string σε λίστα ακεραίων
        digits = [int(d) for d in afm]
        
        # --- MODULO 11 ALGORITHM ---
        #  Πολλαπλασιασμός των 8 πρώτων ψηφίων με δυνάμεις του 2

        sum_val = sum(digits[i] * (2**(8-i)) for i in range(8))
        
        #  Υπολογισμός υπολοίπου
        remainder = sum_val % 11
        
        #  Κανονικοποίηση -Αν το υπόλοιπο είναι 10, το check digit γίνεται 0
        check_digit = remainder % 10
        
        # Σύγκριση με το 9ο ψηφίο ελέγχου
        return check_digit == digits[8]

    except Exception:
        # Σε περίπτωση κάποιου edge case, επιστρέφουμε False για Fail Safe
        return False