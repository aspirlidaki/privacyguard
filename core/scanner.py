import os
import re
import math
from .patterns import PATTERNS, validate_afm, validate_luhn, validate_iban

def calculate_shannon_entropy(data):
    """Calculates randomness for unknown secret detection."""
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
                        if name == 'Greek AFM (VAT)': is_valid = validate_afm(payload)
                        elif name in ['Greek AMKA', 'Credit Card']: is_valid = validate_luhn(payload)
                        elif name == 'Greek IBAN': is_valid = validate_iban(payload)
                        
                        if is_valid:
                            results.append((name, payload[:4] + "****")) # Data Masking
    except Exception: pass
    return results

def scan_directory(path):
    all_findings = {}
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            findings = scan_file(full_path)
            if findings: all_findings[full_path] = findings
    return all_findings
