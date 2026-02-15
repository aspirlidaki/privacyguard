import os
import re
import math
import logging
from .patterns import PATTERNS, validate_afm, validate_luhn, validate_iban

def calculate_shannon_entropy(data):
    """Calculates the Shannon entropy of a string."""
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def scan_file(filepath):
    results = []
    try:
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.exe', '.dll', '.so', '.pdf', '.zip')):
            return []

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                # 1. Pattern Matching (Regex)
                for name, pattern in PATTERNS.items():
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        payload = match.group()
                        is_valid = True
                        
                        # Apply specialized math validation
                        if name == 'Greek AFM (VAT)':
                            is_valid = validate_afm(payload)
                        elif name in ['Greek AMKA', 'Credit Card']:
                            is_valid = validate_luhn(payload)
                        elif name == 'Greek IBAN':
                            is_valid = validate_iban(payload)

                        if is_valid:
                            results.append({
                                'file': filepath,
                                'line': line_num,
                                'type': name,
                                'payload': payload[:4] + "****" # Data Masking
                            })

                # 2. Entropy Check (Secondary detection layer)
                words = line.split()
                for word in words:
                    if len(word) > 20 and calculate_shannon_entropy(word) > 4.5:
                        if not word.startswith('GR'): 
                            results.append({
                                'file': filepath,
                                'line': line_num,
                                'type': 'High Entropy String (Potential Secret)',
                                'payload': word[:4] + "****"
                            })

    except Exception as e:
        logging.error(f"Error scanning {filepath}: {str(e)}")
    
    return results

def scan_directory(directory_path):
    all_findings = {} # Changed to dict for main.py compatibility
    for root, _, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            findings = scan_file(filepath)
            if findings:
                # Format for main.py: {path: [(type, payload), ...]}
                all_findings[filepath] = [(f['type'], f['payload']) for f in findings]
    return all_findings
