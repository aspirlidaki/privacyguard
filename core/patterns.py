"""
PrivacyGuard Pro - Detection Patterns & Validation Logic
------------------------------------------------------
Author: Anastasia S.
"""

# --- 1. DETECTION SIGNATURES (REGEX) ---
PATTERNS = {
    'Google API Key': r'AIza[0-9A-Za-z-_]{35}',
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    'GitHub Token': r'ghp_[a-zA-Z0-9]{36}',
    'Greek AFM (VAT)': r'\b\d{9}\b',
    'Greek AMKA': r'\b\d{11}\b',        # ΝΕΟ: 11 Ψηφία
    'Greek IBAN': r'\bGR\d{25}\b',      # ΝΕΟ: GR + 25 ψηφία
}

# --- 2. VALIDATION ALGORITHMS ---

def validate_afm(afm: str) -> bool:
    """Επαλήθευση Ελληνικού ΑΦΜ (Modulo 11)."""
    if not afm.isdigit() or len(afm) != 9 or afm == "000000000":
        return False
    try:
        digits = [int(d) for d in afm]
        sum_val = sum(digits[i] * (2**(8-i)) for i in range(8))
        remainder = sum_val % 11
        check_digit = remainder % 10
        return check_digit == digits[8]
    except Exception:
        return False

def validate_amka(amka: str) -> bool:
    """Επαλήθευση ΑΜΚΑ (Luhn Algorithm)."""
    if not amka.isdigit() or len(amka) != 11:
        return False
    
    # Luhn Algorithm implementation
    digits = [int(d) for d in amka]
    checksum = 0
    for i in range(len(digits) - 1, -1, -1):
        n = digits[i]
        if (len(digits) - i) % 2 == 0:  # Κάθε δεύτερο ψηφίο από το τέλος
            n *= 2
            if n > 9:
                n -= 9
        checksum += n
        
    return checksum % 10 == 0

def validate_iban(iban: str) -> bool:
    """Επαλήθευση Ελληνικού IBAN (Modulo 97)."""
    # Αφαιρούμε κενά και κάνουμε κεφαλαία
    iban = iban.replace(" ", "").upper()
    
    if len(iban) != 27 or not iban.startswith("GR"):
        return False
        
    # Μετακίνηση των 4 πρώτων χαρακτήρων (GRxx) στο τέλος
    rearranged = iban[4:] + iban[:4]
    
    # Μετατροπή γραμμάτων σε αριθμούς (A=10, B=11, ..., Z=35)
    numeric_string = ""
    for char in rearranged:
        if char.isdigit():
            numeric_string += char
        else:
            numeric_string += str(ord(char) - 55)
            
    # Υπολογισμός Modulo 97
    return int(numeric_string) % 97 == 1
