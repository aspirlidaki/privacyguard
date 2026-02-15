import os
import re
import math
import logging
from .patterns import PATTERNS, validate_afm, validate_luhn, validate_iban

def calculate_shannon_entropy(data):
    """Calculates string randomness using Shannon entropy."""
    if not data: return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def scan_file(filepath):
    results = []
    try:
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.exe', '.pdf', '.zip')):
            return []

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for name, pattern in PATTERNS.items():
                    for match in re.finditer(pattern, line):
                        payload = match.group()
                        is_valid = True
                        if name == 'Greek AFM (VAT)':
                            is_valid = validate_afm(payload)
                        elif name in ['Greek AMKA', 'Credit Card']:
                            is_valid = validate_luhn(payload)
                        elif name == 'Greek IBAN':
                            is_valid = validate_iban(payload)

                        if is_valid:
                            results.append({
                                'type': name,
                                'payload': payload[:4] + "****" # Data Masking
                            })
    except Exception as e:
        logging.error(f"Error scanning {filepath}: {str(e)}")
    return results

def scan_directory(directory_path):
    all_findings = {} # Must return a dict for main.py
    for root, _, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            findings = scan_file(filepath)
            if findings:
                all_findings[filepath] = [(f['type'], f['payload']) for f in findings]
    return all_findings
