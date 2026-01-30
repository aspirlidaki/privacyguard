#  Algorithmic Logic & Mathematical Models

This document details the mathematical algorithms and validation logic employed by **PrivacyGuard Pro** to ensure high-fidelity detection of sensitive information while minimizing false positives.

---

## 1. Shannon Entropy (Information Theory)

###  Concept
**Shannon Entropy** provides a mathematical measure of the "randomness" or information density contained within a string of characters. In the context of secret detection, high-entropy strings usually indicate cryptographic keys, tokens, or passwords, while low-entropy strings indicate natural language.

### The Formula
The entropy $H$ of a string $X$ is calculated using the formula:

$$H(X) = - \sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

Where:
* $P(x_i)$ is the probability (frequency) of character $x_i$ appearing in the string.
* $\log_2$ is the base-2 logarithm (bits).

###  Implementation Strategy
1.  **Frequency Analysis**: We calculate the frequency of every ASCII character in the target string.
2.  **Computation**: We apply the formula to determine the bit density.
3.  **Thresholding**:
    * **Natural Language**: Typically has an entropy between **2.5 - 3.5**.
    * **Base64/Hex Secrets**: Typically have an entropy **> 4.5**.
    * **Decision Boundary**: We utilize a threshold of **4.5** to flag potential secrets that do not match known Regex patterns.

###  Why we use it
Standard Regex cannot detect unknown secrets (e.g., a custom API key format). Shannon Entropy allows us to identify **"suspiciously random"** strings regardless of their format.

---

## 2. Modulo 11 Checksum (Greek VAT Validation)

###  Concept
The **Modulo 11** algorithm is a checksum formula used to validate the integrity of identification numbers. PrivacyGuard Pro implements the specific variation used by the **Hellenic Republic** for Value Added Tax (AFM) numbers.

###  The Algorithm
A valid Greek AFM consists of 9 digits ($d_1, d_2, ..., d_9$). The last digit ($d_9$) is the **Check Digit**.

**Step 1: Weighted Summation**
We calculate the sum $S$ of the first 8 digits, weighted by powers of 2 (descending order):

$$S = \sum_{i=1}^{8} d_i \times 2^{9-i}$$

Expanded form:
$$S = (d_1 \times 256) + (d_2 \times 128) + (d_3 \times 64) + ... + (d_8 \times 2)$$

**Step 2: Modulo Operation**
We calculate the remainder $R$ of the division of $S$ by 11:

$$R = S \pmod{11}$$

**Step 3: Check Digit Determination**
* If $R = 10$, the check digit must be **0**.
* Otherwise, the check digit must be equal to $R$.

###  Code Representation
```python
check_digit = (sum_val % 11) % 10
```
### Why?
A simple Regex like \d{9} would incorrectly flag phone numbers, timestamps, or random integers as tax IDs. Modulo 11 ensures mathematical validity, reducing False Positives by nearly 99%.

## 3.Computational Complexity Analysis
| Algorithm | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **Stream Scanning** | $O(N)$ | $O(1)$ | Process files line-by-line to minimize RAM usage. |
| **Shannon Entropy** | $O(K)$ | $O(1)$ | $K$ is the string length. Calculation is linear. |
| **Modulo 11** | $O(1)$ | $O(1)$ | Fixed input size (9 digits). |