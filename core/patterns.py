import re

# Αυτά είναι τα "μοτίβα" (Regex) 

PATTERNS = {
    'Google API Key': r'AIza[0-9A-Za-z-_]{35}',
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    'GitHub Token': r'ghp_[a-zA-Z0-9]{36}',
    'Greek AFM (VAT)': r'\b\d{9}\b',  # Ψάχνει για 9 συνεχή ψηφία
}

def validate_afm(afm):
    """
  #  Εδώ υλοποιούμε τον αλγόριθμο Modulo 11.
    """
    if not afm.isdigit() or len(afm) != 9:
        return False
    
    digits = [int(d) for d in afm]
    # Ο μαθηματικός έλεγχος του ΑΦΜ
    sum_val = sum(digits[i] * (2**(8-i)) for i in range(8))
    check_digit = (sum_val % 11) % 10
    
    return check_digit == digits[8]