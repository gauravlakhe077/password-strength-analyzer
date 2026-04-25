# 🔐 Password Strength Analyzer with Attack Simulation

## 📌 Overview
This project analyzes password strength and demonstrates how weak passwords can be cracked using real-world tools like John the Ripper.

---

## 🎯 Features
- Password strength checking using Regex
- Advanced analysis using zxcvbn
- Attack simulation using John the Ripper
- Dictionary-based password cracking (rockyou.txt)

---

## 🛠️ Technologies Used
- Python
- Kali Linux
- John the Ripper
- zxcvbn library

---

## ⚙️ How It Works

### 1. Password Analysis
- Checks length, uppercase, lowercase, digits, symbols
- Uses zxcvbn for advanced scoring

### 2. Attack Simulation
- Converts password into hash
- Uses wordlist attack
- Attempts to crack password

---

## ▶️ How to Run

```bash
source venv/bin/activate
python main.py
