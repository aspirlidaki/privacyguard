# PrivacyGuard 
**Advanced Static Analysis Security Testing (SAST) Tool for Secret Detection and PII Compliance**

---

## Abstract

PrivacyGuard is a static analysis security tool designed to detect sensitive information, hardcoded credentials, and Personally Identifiable Information (PII) within source code repositories. The tool aims to mitigate credential leakage risks and support compliance with data protection regulations, such as the General Data Protection Regulation (GDPR). It employs a multi-layered detection approach that combines pattern matching, entropy analysis, and mathematical validation in order to reduce false positives while maintaining high detection accuracy.

---

## 1. Introduction

The accidental exposure of sensitive data within source code repositories constitutes a critical security risk. Hardcoded credentials, API keys, and PII may lead to unauthorized access, data breaches, and regulatory non-compliance. Static Application Security Testing (SAST) tools provide an effective method for identifying such risks early in the development lifecycle.

PrivacyGuard  addresses this problem by offering an extensible and automated scanning solution capable of detecting both known and unknown secret patterns, with particular emphasis on PII validation and entropy-based analysis.

---

## 2. System Overview

PrivacyGuard  performs recursive directory scanning and analyzes source files using a modular detection architecture. The system is implemented in Python and is designed to be lightweight, extensible, and suitable for integration into CI/CD pipelines.

---

## 3. Detection Methodology

### 3.1 Pattern-Based Detection

The Pattern Engine utilizes optimized regular expressions to identify known formats of sensitive data, including API keys, authentication tokens, and credentials. This approach enables fast and deterministic detection of well-defined secret structures.

### 3.2 Validation-Based Detection

To minimize false positives, PrivacyGuard  applies mathematical validation techniques where applicable. A notable example is the validation of Greek VAT numbers (AFM) using the Modulo 11 checksum algorithm, ensuring that detected identifiers conform to official specifications.

### 3.3 Entropy-Based Detection

The Entropy Engine computes Shannon Entropy to identify strings exhibiting high randomness. This technique enables the detection of previously unknown or obfuscated secrets, such as cryptographic keys, even in the absence of predefined patterns.

---
## 4. Architecture and Implementation
The tool follows a modular architecture, separating concerns across multiple components:

```text
privacyguard/
├── .github/
│   └── workflows/
│       └── tests.yml         # Continuous Integration configuration
├── core/
│   ├── patterns.py           # Detection patterns and validation logic
│   ├── scanner.py            # File traversal and analysis engine
│   ├── logger.py             # Logging configuration and severity handling
│   └── __init__.py
├── tests/                    # Automated unit tests
├── samples/                  # Demonstration and test input files
├── main.py                   # Command-line interface entry point
├── requirements.txt          # Dependency specification
└── SECURITY.md               # Responsible disclosure policy
```

## 5. Logging and Auditability
PrivacyGuard Pro provides structured logging to support traceability and post-scan analysis. Logging is implemented with severity levels (INFO, WARNING, ERROR) in order to distinguish between informational messages, potential security findings, and critical errors.

All scan activities and detection events are recorded in a dedicated log file (scanner.log), enabling auditability and facilitating debugging, compliance verification, and forensic analysis.

---


## 6. Continuous Integration Support
The tool is designed to integrate seamlessly with Continuous Integration and Continuous Deployment (CI/CD) pipelines. GitHub Actions are used to automatically execute unit tests on each commit and pull request.

This approach ensures detection accuracy, prevents regressions, and promotes reproducibility and reliability throughout the development lifecycle.

---


## 7. Usage
PrivacyGuard Pro can be executed through a command-line interface by specifying the target directory to be scanned.

Bash
python3 main.py --path ./samples --json
The above command performs a recursive scan of the specified directory and outputs the detected findings in JSON format.

---


## 8. Security and Ethical Considerations
The tool adheres to the Principle of Least Privilege and includes a responsible vulnerability disclosure policy.

Disclaimer: This tool is intended solely for authorized security auditing and educational purposes. The author assumes no responsibility for misuse or damage resulting from improper or unauthorized use of the tool.

---


## 9. Conclusion
PrivacyGuard Pro demonstrates the effectiveness of combining pattern-based detection, entropy analysis, and mathematical validation techniques in static application security testing. Its modular architecture, logging capabilities, and CI/CD integration make it suitable for both academic research and practical security auditing scenarios.

---


### Author
Anastasia S. Cybersecurity Enthusiast & Developer GitHub: 
@aspirlidaki
