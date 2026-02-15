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
    'Azure Secret': r'[a-zA-Z0-9]{3}~[a-zA-Z0-9.-_]{34}',
    'Credit Card': r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b',
    'Greek AFM (VAT)': r'\b\d{9}\b',
    'Greek AMKA': r'\b\d{11}\b',
    'Greek IBAN': r'\bGR\d{25}\b',
}

# --- 2. VALIDATION ALGORITHMS ---

def validate_afm(afm: str) -> bool:
    """Επαλήθευση Ελληνικού ΑΦΜ (Modulo 11)."""
    if not afm.isdigit() or len(afm) != 9 or afm == "000000000":
        return False
    try:
        digits = [int(d) for d in afm]
        # Weighted sum based on descending powers of 2
        sum_val = sum(digits[i] * (2**(8-i)) for i in range(8))
        remainder = sum_val % 11
        check_digit = remainder % 10
        return check_digit == digits[8]
    except Exception:
        return False

def validate_luhn(number: str) -> bool:
    """Generic Luhn Algorithm used for AMKA and Credit Cards."""
    if not number.isdigit():
        return False
    digits = [int(d) for d in number]
    checksum = 0
    for i in range(len(digits) - 1, -1, -1):
        n = digits[i]
        if (len(digits) - i) % 2 == 0:  
            n *= 2
            if n > 9:
                n -= 9
        checksum += n
    return checksum % 10 == 0

# Alias for AMKA compatibility
validate_amka = validate_luhn

def validate_iban(iban: str) -> bool:
    """Επαλήθευση Ελληνικού IBAN (Modulo 97)."""
    iban = iban.replace(" ", "").upper()
    if len(iban) != 27 or not iban.startswith("GR"):
        return False
    rearranged = iban[4:] + iban[:4]
    numeric_string = "".join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged)
    return int(numeric_string) % 97 == 1
