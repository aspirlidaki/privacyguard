import argparse
import sys
from core.scanner import scan_directory

def main():
    # Δημιουργούμε έναν "parser" για να δέχεται εντολές από το τερματικό
    parser = argparse.ArgumentParser(description=" PrivacyGuard: Sensitive Data & Secret Scanner")
    parser.add_argument("--path", help="Το path του φακέλου που θέλετε να σκανάρετε", required=True)
    
    args = parser.parse_args()

    print(f"\n[+] Ξεκινάει το σκανάρισμα στο: {args.path}")
    print("-" * 50)

    # Καλούμε τη συνάρτηση σκαναρίσματος που φτιάξαμε στο scanner.py
    findings = scan_directory(args.path)

    if not findings:
        print("[✅] Συγχαρητήρια! Δεν βρέθηκαν ευαίσθητα δεδομένα.")
    else:
        total_issues = 0
        for file_path, issues in findings.items():
            print(f"\n Αρχείο: {file_path}")
            for issue_type, value in issues:
                # Εδώ κρύβουμε ένα μέρος του κωδικού για ασφάλεια στο report
                masked_value = value[:4] + "*" * (len(value) - 4)
                print(f"   [⚠️] Βρέθηκε {issue_type}: {masked_value}")
                total_issues += 1
        
        print("-" * 50)
        print(f"[!] Σύνολο ευρημάτων: {total_issues}")

if __name__ == "__main__":
    main()