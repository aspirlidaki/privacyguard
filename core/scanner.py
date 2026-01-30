"""
PrivacyGuard  - Core Scanner Logic
-------------------------------------
Author: Anastasia S.
Description: 
    Η μηχανή σάρωσης. Διατρέχει αρχεία, ελέγχει για known patterns 
    και υπολογίζει Shannon Entropy για άγνωστα secrets.

Performance Note:
    Χρησιμοποιω Lazy Loading (γραμμή-γραμμή) για να μην υπερφορτώσω τη RAM.
"""

import os
import re
import math
from core.patterns import PATTERNS, validate_afm
from core.logger import logger

# Λίστα με φακέλους που αγνοώ για ταχύτητα (Performance Optimization)
IGNORED_DIRS = {'.git', '.idea', '__pycache__', 'node_modules', 'venv', '.env'}
# Αρχεία που δεν είναι text (Binary/Media) και πρέπει να αγνοηθούν
IGNORED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.exe', '.dll', '.so', '.zip', '.pdf'}

def calculate_entropy(data: str) -> float:
    """
    Υπολογίζει το Shannon Entropy.
    Security Value: 
        Strings με εντροπία > 4.5 είναι συνήθως κρυπτογραφικά κλειδιά ή tokens.
    """
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def is_binary_file(file_path: str) -> bool:
    """
    Heuristic έλεγχος για το αν ένα αρχείο είναι binary.
    Διαβάζει τα πρώτα 1024 bytes και ψάχνει για NULL bytes.
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            return b'\0' in chunk
    except Exception:
        return True # Αν δεν ανοίγει, το θεωρούμε binary για ασφάλεια.

def scan_file(file_path: str):
    """
    Σκανάρει ένα αρχείο γραμμή-γραμμή για patterns και high entropy strings.
    """
    findings = []
    
    # 1. Skip Binary Files (Αποφυγή θορύβου και λαθών)
    if any(file_path.endswith(ext) for ext in IGNORED_EXTENSIONS) or is_binary_file(file_path):
        logger.debug(f"Skipping binary/media file: {file_path}")
        return findings

    try:
        # 2. Memory Efficient Reading (Line-by-Line)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                
                # A. Pattern Matching (Regex)
                for name, pattern in PATTERNS.items():
                    matches = re.findall(pattern, line)
                    for match in matches:
                        # Αν είναι ΑΦΜ, τρέχουμε Validation
                        if name == 'Greek AFM (VAT)':
                            if validate_afm(match):
                                findings.append((name, match))
                        else:
                            findings.append((name, match))
                
                # B. Entropy Analysis (Για άγνωστα secrets)
                # Ελέγχώ λέξεις > 20 χαρακτήρων (πιθανά keys)
                for word in line.split():
                    if len(word) > 20 and ' ' not in word:
                        entropy = calculate_entropy(word)
                        # Threshold 4.5: Συνήθης τιμή για Base64 tokens
                        if entropy > 4.5:
                            # Αποφεύγω διπλοεγγραφές αν το έπιασε ήδη κάποιο regex
                            if not any(word in f[1] for f in findings):
                                findings.append(('High Entropy String (Unknown Secret)', word))

    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        
    return findings

def scan_directory(directory_path: str):
    """
    Αναδρομική σάρωση φακέλων με έξυπνη εξαίρεση (Smart Exclusions).
    """
    all_results = {}
    
    # os.walk: Τρέχει σε όλο το δέντρο φακέλων
    for root, dirs, files in os.walk(directory_path):
        
        # --- Performance Hack ---
        # Τροποποιώ τη λίστα dirs IN-PLACE για να ΜΗΝ μπει καν σε φακέλους 
        # όπως το .git ή το node_modules. Εξοικονομεί τεράστιο χρόνο.
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Σκανάρισμα αρχείου
            results = scan_file(file_path)
            
            if results:
                all_results[file_path] = results
                
    return all_results