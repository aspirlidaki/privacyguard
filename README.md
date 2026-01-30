# 🛡️ PrivacyGuard 
> **Advanced Static Analysis Security Testing (SAST) Tool for Secret Detection & PII Compliance.**

![Build Status](https://github.com/aspirlidaki/privacyguard/actions/workflows/tests.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview
**PrivacyGuard** is a high-performance security scanner designed to identify sensitive information, hardcoded credentials, and Personal Identifiable Information (PII) within source code and directories. It helps developers and security engineers prevent **Credential Leakage** and ensure **GDPR Compliance**.



---

## ✨ Key Features
* **Multi-Layered Detection**: Combines Regex patterns, Shannon Entropy, and Mathematical Validation.
* **Greek PII Support**: Specialized logic for validating Greek VAT numbers (AFM) using the **Modulo 11** algorithm.
* **Entropy-Based Discovery**: Detects high-entropy strings (e.g., AWS/Google Keys) even without predefined patterns.
* **Professional Logging**: Comprehensive audit trails in `scanner.log` with severity levels (INFO, WARNING, ERROR).
* **CI/CD Ready**: Integrated GitHub Actions for automated quality assurance.

---

## 🛠️ Technical Architecture

### 1. Detection Engines
* **Pattern Engine**: Utilizes optimized Regular Expressions for known formats (API Keys, Tokens).
* **Validation Engine**: Reduces False Positives by verifying checksums (e.g., Modulo 11 for Greek AFM).
* **Entropy Engine**: Calculates **Shannon Entropy** to flag suspicious high-randomness strings.



### 2. Modular Structure
```text
privacyguard/
├── core/
│   ├── patterns.py   # Detection logic & Regex
│   ├── scanner.py    # Directory traversal & file analysis
│   └── logger.py     # Professional logging configuration
├── tests/            # Automated Unit Tests
├── samples/          # Test files for demonstration
└── main.py           # CLI Entry point

🚀 Getting Started
Prerequisites
Python 3.10 or higher

Git

Installation
Bash
git clone [https://github.com/aspirlidaki/privacyguard.git](https://github.com/aspirlidaki/privacyguard.git)
cd privacyguard
pip install -r requirements.txt
Usage
Run the scanner on a specific directory:

Bash
python3 main.py --path ./samples --json
🧪 Testing
We use automated unit tests to ensure detection accuracy:

Bash
python3 -m unittest discover tests
🛡️ Security & Compliance
This tool follows the Principle of Least Privilege and includes a SECURITY.md for responsible vulnerability disclosure.

Disclaimer: This tool is for authorized security auditing purposes only.

👩‍💻 Author
Anastasia S. - Cybersecurity Enthusiast & Developer

GitHub: @aspirlidaki