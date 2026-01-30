#!/usr/bin/env python3
"""
PrivacyGuard - Entry Point
------------------------------
Author: Anastasia S.
Description: Κεντρικό σημείο εκτέλεσης του SAST scanner.
Security Note: Χειρίζεται ευαίσθητα δεδομένα, γι' αυτό εφαρμόζω
αυστηρό Data Masking στα logs.
"""

import argparse
import json
import sys
import os

# Διαχωρισμός λογικής (Core) από το Interface (CLI)
from core.logger import logger 
from core.scanner import scan_directory

def main():
    # --- 1. CLI CONFIGURATION ---
    # Ορίζω το Interface. Ένα καλό Security Tool πρέπει να είναι σαφές στη χρήση του.
    parser = argparse.ArgumentParser(
        description="🛡️  PrivacyGuard Pro: Advanced Static Analysis Security Tool (SAST)",
        epilog="Security is a process, not a product."
    )
    
    parser.add_argument(
        "--path", 
        required=True, 
        help="Target directory for security auditing"
    )
    
    parser.add_argument(
        "--json", 
        help="Export findings to results.json (useful for CI/CD pipelines)", 
        action="store_true"
    )
    
    args = parser.parse_args()

    # --- 2. PRE-FLIGHT CHECKS ---
    # Ελέγχω  αν υπάρχει ο φάκελος πριν ξεκινήσουμε 
    if not os.path.isdir(args.path):
        logger.error(f"Invalid directory path: {args.path}")
        sys.exit(1)

    # --- 3. EXECUTION PHASE ---
    logger.info("="*50)
    logger.info(f"🚀 Initializing Security Scan on: {os.path.abspath(args.path)}")
    logger.info("="*50)
    
    try:
        # Καλώ τον scanner. Αν υπάρξει permission error ή corruption, το πιάνώ εδώ.
        findings = scan_directory(args.path)
        
    except KeyboardInterrupt:
        # Χειρισμός του Ctrl+C από τον χρήστη για ομαλό τερματισμό
        logger.warning("\nScan interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        # Catch-all για απρόβλεπτα λάθη 
        logger.error(f"Critical Runtime Error: {e}")
        sys.exit(1)

    # --- 4. REPORTING PHASE ---
    if not findings:
        # Green state: Δεν βρέθηκαν ευρήματα
        logger.info("✅ Scan completed successfully. System appears Clean.")
    else:
        # Red state: Βρέθηκαν ευρήματα
        logger.warning(f"⚠️  Potential Security Issues Detected: {len(findings)} files affected.")
        
        for file_path, issues in findings.items():
            logger.warning(f"📂 File: {file_path}")
            
            for issue_type, value in issues:
                # --- SECURITY CRITICAL: DATA MASKING ---
                
                # Δείχνω μόνο τα 4 πρώτα ψηφία για verification.
                masked_value = f"{value[:4]}****" if len(value) > 4 else "****"
                
                logger.warning(f"  └── [TYPE: {issue_type}] | [PAYLOAD: {masked_value}]")

    # --- 5. ARTIFACT GENERATION ---
    # Εξαγωγή σε JSON για να μπορεί να διαβαστεί από άλλα εργαλεία 
    if args.json:
        try:
            output_file = "results.json"
            with open(output_file, "w") as f:
                json.dump(findings, f, indent=4)
            logger.info(f"💾 Audit Artifact saved to: {output_file}")
        except IOError as e:
            logger.error(f"Failed to write audit artifact: {e}")

    # Στο CI/CD, αν βρούμε issues, μερικές φορές θέλουμε να σπάσουμε το build (exit code 1).
    # 0 (success execution) 
    if findings:
        logger.info(" Action Required: Please review the findings above.")
    
    logger.info(" Security Scan Finished.")

if __name__ == "__main__":
    main()