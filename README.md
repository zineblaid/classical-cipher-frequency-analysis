# Classical Cipher Decryption Using Frequency Analysis

## Project Overview

This project implements frequency analysis techniques in Python to attempt to decrypt classical ciphers.

It supports three types of ciphers:

- **Caesar Cipher**
- **Affine Cipher**
- **Monoalphabetic Substitution Cipher**

The program analyzes the frequency of letters in an encrypted message and uses predefined letter-frequency patterns to generate probable plaintexts.

##  Objectives

- Explore classical cryptography and cryptanalysis.
- Understand letter frequency analysis.
- Implement decryption techniques for classical ciphers.
- Apply modular arithmetic and modular inverses.
- Compare frequency-based approaches for different cipher types.
- Practice Python programming and problem-solving.

##  Supported Algorithms

### 1. Caesar Cipher

The program identifies the most frequent letter in the ciphertext and compares it with a reference letter to estimate the encryption shift.

It then applies the estimated shift to generate a possible plaintext.

### 2. Affine Cipher

The program tests possible values of the affine cipher keys `a` and `b`.

It uses the greatest common divisor (GCD) to identify valid values of `a` and calculates the modular inverse required for decryption.

Candidate plaintexts are generated and filtered using letter-frequency assumptions.

### 3. Monoalphabetic Substitution Cipher

The program ranks ciphertext letters by their frequency and maps them to a predefined letter-frequency sequence.

This produces an estimated substitution mapping and a probable plaintext.

##  Language Options

The program provides English and Arabic language options for frequency-based analysis.

**Note:** Arabic decryption is not fully implemented in the current version. The Caesar and Affine functions use English alphabet operations and modulo 26, so the Arabic option should be considered experimental.

##  Technologies Used

- **Language:** Python 3
- **Library:** `collections.Counter`
- **Concepts:** Classical Cryptography, Cryptanalysis, Frequency Analysis, Modular Arithmetic, Greatest Common Divisor, Modular Inverse

##  How to Run

### Requirements

- Python 3.x

No external packages are required because `collections.Counter` is included in Python's standard library.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/classical-cipher-frequency-analysis.git
   ```

2. Open the project directory:

   ```bash
   cd classical-cipher-frequency-analysis
   ```

3. Run the program:

   ```bash
   python main.py
   ```

##  Usage

When the program starts, select one of the available options:

```text
--- Frequency Analysis Decryption ---
1 - Caesar
2 - Affine
3 - Substitution
4 - Exit
```

Then:

1. Select the cipher to analyze.
2. Enter the encrypted message.
3. Choose the language option.
4. Examine the probable plaintext or candidate solutions.
5. Select `4` to exit.

##  Key Concepts

- Frequency analysis
- Caesar cipher
- Affine cipher
- Monoalphabetic substitution
- Modular arithmetic
- Greatest common divisor (GCD)
- Modular inverse
- Basic cryptanalysis

##  Limitations

Frequency analysis does not guarantee correct decryption. Its effectiveness depends on ciphertext length, language characteristics, and the accuracy of the frequency assumptions.

The current implementation is intended for educational purposes and does not provide reliable support for decrypting Arabic text.

It is designed to demonstrate classical cryptanalysis techniques, not to break modern encryption algorithms.

##  Author

ZINEB OULAD LAID

Software Engineering Student

##  License

This project is intended for educational and learning purposes.
