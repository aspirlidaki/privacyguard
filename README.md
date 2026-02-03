cat << 'EOF' > README.md
# PrivacyGuard 

[![CI Tests](https://github.com/aspirlidaki/privacyguard/actions/workflows/tests.yml/badge.svg)](https://github.com/aspirlidaki/privacyguard/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-SAST-red)

> **Advanced Static Application Security Testing (SAST)** tool designed to detect hardcoded secrets, API keys, and PII with a focus on Greek Tax Identification Numbers (AFM).

---

##  Documentation

This repository contains professional-grade documentation for auditors and developers:

*  **[Technical Whitepaper](WHITEPAPER.md)**: Full system architecture, methodology, and abstract.
*  **[Algorithmic Logic](ALGORITHMS.md)**: Deep dive into **Shannon Entropy** and **Modulo 11** math models.
*  **[Security Policy](SECURITY.md)**: Disclosure and vulnerability reporting.

---

##  Key Features

* **Smart Detection**: Identifies Google Keys, AWS Keys, and GitHub Tokens using regex signatures.
* **Mathematical Validation**: Implements **Modulo 11** algorithm to verify Greek AFM (VAT) numbers, eliminating false positives from random 9-digit numbers.
* **Entropy Analysis**: Uses **Shannon Entropy** to detect unknown high-entropy secrets (e.g., random passwords or keys without specific patterns).
* **Forensic Logging**: Keeps a detailed audit trail in `scanner.log`.
* **CI/CD Ready**: Exports results to JSON for easy integration with GitHub Actions or Jenkins.

---

##  Installation

PrivacyGuard Pro is lightweight and relies on the Python Standard Library.

```bash
# 1. Clone the repository
git clone [https://github.com/aspirlidaki/privacyguard.git](https://github.com/aspirlidaki/privacyguard.git)

# 2. Navigate to the directory
cd privacyguard
```
## Usage
1. Quick Scan
Run a security scan on a specific directory and view results in the terminal.

```Bash
python3 main.py --path /path/to/target/directory
```

## 2. Audit Mode (JSON Export)
Run a scan and export the findings to a results.json file.

```Bash
python3 main.py --path . --json
```
 Project Structure
```text
privacyguard/
├── .github/workflows/    # CI/CD Automation (Tests)
├── core/                 # The Engine
│   ├── patterns.py       # Regex & Math Logic (Modulo 11)
│   ├── scanner.py        # Entropy & File Scanning
│   └── logger.py         # Audit Logging
├── tests/                # Unit Tests
├── ALGORITHMS.md         # Math Documentation
├── WHITEPAPER.md         # Technical Documentation
├── main.py               # Entry Point
└── requirements.txt      # Dependencies
```
## Disclaimer
This tool is intended for defensive security purposes (Blue Team) and code auditing. The author assumes no responsibility for unauthorized use.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Author
Anastasia S. | GitHub Profile EOF
---

## 🐳 Docker Support

You can run PrivacyGuard Pro inside a container without installing Python locally.

### 1. Build the Image
```bash
docker build -t privacyguard:v1 .