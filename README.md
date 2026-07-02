# 🔐 AES Encryption Demo in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Educational-orange)

A simple Python project demonstrating **AES (Advanced Encryption Standard)** encryption and decryption using the **PyCryptodome** library.

---

## 📖 Overview

This project demonstrates the basic workflow of **AES symmetric encryption**:

- Accept plaintext from the user
- Encrypt the plaintext
- Decrypt the ciphertext
- Verify that the decrypted text matches the original input

> **Note:** This project uses **AES in ECB mode** for educational purposes. ECB mode is not recommended for production use because it does not conceal data patterns.

---

## ✨ Features

- AES Encryption
- AES Decryption
- PKCS#7 Padding
- Command-Line Interface
- Beginner-Friendly Implementation

---

## 🛠 Technologies Used

- Python 3
- PyCryptodome

---

## 🚀 Installation

Install the dependency:

```bash
pip install pycryptodome
```

Run the program:

```bash
python aes_demo.py
```

---

## 📂 Repository Structure

```
aes-encryption-demo-python
│
├── aes_demo.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📚 Learning Objectives

- Understand symmetric key encryption
- Learn AES encryption fundamentals
- Practice encryption and decryption using Python
- Learn how block cipher padding works

---

## ⚠ Disclaimer

This repository was created for educational purposes.

For real-world applications, secure modes such as **AES-CBC** or **AES-GCM** should be used instead of ECB.

---

