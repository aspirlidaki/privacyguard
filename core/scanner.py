import os
import re
from core.patterns import PATTERNS, validate_afm
import math

def scan_file(file_path):
    """Σκανάρει ένα αρχείο για patterns και επιστρέφει τα ευρήματα."""
    findings = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for name, pattern in PATTERNS.items():
                matches = re.findall(pattern, content)
                for match in matches:
                    # Αν βρει ΑΦΜ, τρέχει τον έξτρα έλεγχο Modulo 11
                    if name == 'Greek AFM (VAT)':
                        if validate_afm(match):
                            findings.append((name, match))
                    else:
                        findings.append((name, match))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return findings

def scan_directory(directory_path):
    """Πηγαίνει σε όλους τους υποφακέλους και σκανάρει κάθε αρχείο."""
    all_results = {}
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Αγνοούμε τον φάκελο .git για ταχύτητα και ασφάλεια
            if '.git' in root:
                continue
                
            file_path = os.path.join(root, file)
            results = scan_file(file_path)
            
            if results:
                all_results[file_path] = results
                
    return all_results
def calculate_entropy(data):
    """Υπολογίζει το Shannon Entropy ενός string. 
    Όσο πιο υψηλό (πάνω από 4.0), τόσο πιο 'τυχαίο' είναι το κείμενο."""
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy