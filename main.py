import argparse
import json
from core.scanner import scan_directory

def main():
    parser = argparse.ArgumentParser(description="🛡️ PrivacyGuard Pro")
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", help="Αποθήκευση αποτελεσμάτων σε JSON", action="store_true")
    
    args = parser.parse_args()
    findings = scan_directory(args.path)

    # Εκτύπωση στο τερματικό
    for file_path, issues in findings.items():
        print(f"\n📍 {file_path}")
        for issue_type, value in issues:
            print(f"   [⚠️] {issue_type}: {value[:6]}...")

    # Export σε JSON αν ζητηθεί
    if args.json:
        with open("results.json", "w") as f:
            json.dump(findings, f, indent=4)
        print("\n[💾] Τα αποτελέσματα αποθηκεύτηκαν στο results.json")

if __name__ == "__main__":
    main()