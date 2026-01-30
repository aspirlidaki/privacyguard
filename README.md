![Tests](https://github.com/aspirlidaki/privacyguard/actions/workflows/tests.yml/badge.svg)
#  PrivacyGuard: Sensitive Data & Secret Scanner
## OVERVIEW
**PrivacyGuard** is a static analysis security tool (SAST) designed to detect hardcoded secrets and sensitive information within source code. This project focuses on identifying leaked API keys and ensuring GDPR compliance by detecting Greek national identifiers (AFM/AMKA).

## Key Features
- **Secret Detection:** Scans for high-entropy strings like AWS keys, GitHub tokens, and Google API keys.
- **GDPR Compliance:** Specialized logic to identify Greek VAT numbers (AFM) and Social Security numbers (AMKA).
- **Validation Engine:** Implements the **Modulo 11 algorithm** to validate Greek identifiers and reduce false positives.
- **Color-coded Reporting:** Clear terminal output for rapid triage of security findings.

##  Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/aspirlidaki/privacyguard.git](https://github.com/aspirlidaki/privacyguard.git)

# Navigate to the directory
cd privacyguard

# Install dependencies (Coming soon)
pip install -r requirements.txt

# Run the scanner
python main.py --path ./your_project_folder.

