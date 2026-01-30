"""
PrivacyGuard - Logging Module
---------------------------------
Description: Κεντρικό σύστημα καταγραφής συμβάντων (Audit Trail).
Security Purpose: 
  - Παρέχει ιχνηλασιμότητα (Traceability) για κάθε ενέργεια του scanner.
  - Διαχωρίζει τα logs κονσόλας (UX) από τα logs αρχείου (Forensics).
"""

import logging
import sys

def setup_logger():
    """
    Διαμορφώνει τον logger για να στέλνει δεδομένα σε αρχείο και οθόνη.
    """
    
    # Χρήση συγκεκριμένου ονόματος για αποφυγή συγκρούσεων με άλλες βιβλιοθήκες
    logger = logging.getLogger("PrivacyGuard")
    logger.setLevel(logging.INFO)

    # --- SINGLETON CHECK ---
    # Ελέγχουμε αν έχουν ήδη οριστεί handlers. Αν ναι, επιστρέφω τον υπάρχοντα logger.
    # Αυτό αποτρέπει την εγγραφή διπλών γραμμών στο log file αν κληθεί η συνάρτηση ξανά.
    if logger.hasHandlers():
        return logger

    # --- FORMATTING ---
    # Format: [TIMESTAMP] [SEVERITY] [MESSAGE]
    # timestamp  για τη συσχέτιση συμβάντων (Incident Response).
    log_format = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # --- 1. CONSOLE HANDLER (Operator View) ---
    # Αυτά τα βλέπει ο χρήστης που τρέχει το εργαλείο
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # --- 2. FILE HANDLER (Forensic Evidence) ---
    # Αυτά μένουν στο δίσκο για ιστορικό έλεγχο.
    #  encoding='utf-8' για Ελληνικά μηνύματα/σχόλια.
    try:
        file_handler = logging.FileHandler("scanner.log", mode='a', encoding='utf-8')
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except PermissionError:
        # Fallback αν δεν έχω δικαιώματα εγγραφής 
        sys.stderr.write(" WARNING: Cannot write to scanner.log. Forensics disabled.\n")

    return logger

#  Δημιουργία του αντικειμένου logger κατά το import
logger = setup_logger()