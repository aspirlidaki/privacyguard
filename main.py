import argparse
import json
import sys
# Εισάγουμε τον logger που φτιάξαμε στο core/logger.py
from core.logger import logger 
from core.scanner import scan_directory

def main():
    parser = argparse.ArgumentParser(description="🛡️ PrivacyGuard Pro: Advanced Security Scanner")
    parser.add_argument("--path", required=True, help="Path to the directory to scan")
    parser.add_argument("--json", help="Export results to results.json", action="store_true")
    
    args = parser.parse_args()

    # Αντί για print, χρησιμοποιούμε logger.info για την έναρξη
    logger.info(f"Starting security scan in directory: {args.path}")
    
    try:
        findings = scan_directory(args.path)
    except Exception as e:
        # Αν κάτι πάει στραβά, το καταγράφουμε ως ERROR
        logger.error(f"Critical error during scanning: {e}")
        sys.exit(1)

    if not findings:
        logger.info("Scan completed: No sensitive data discovered. [CLEAN]")
    else:
        # Καταγραφή των ευρημάτων
        for file_path, issues in findings.items():
            # Χρησιμοποιούμε warning γιατί βρήκαμε κενό ασφαλείας
            logger.warning(f"Potential leak detected in: {file_path}")
            for issue_type, value in issues:
                # Masking του value (δείχνουμε μόνο την αρχή) για ασφάλεια στα logs
                masked = f"{value[:4]}****"
                logger.warning(f"  --> Type: {issue_type} | Preview: {masked}")

    # Export σε JSON
    if args.json:
        try:
            with open("results.json", "w") as f:
                json.dump(findings, f, indent=4)
            logger.info("Results successfully exported to results.json")
        except IOError as e:
            logger.error(f"Failed to export JSON: {e}")

if __name__ == "__main__":
    main()