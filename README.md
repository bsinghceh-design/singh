# Password Policy Testing Toolkit

A Python-based toolkit to **generate password dictionaries**, simulate dictionary attacks, analyze password strength, and check password policy compliance (educational use only).

## Features

- Dictionary generator with simple mutations.
- Uses `wordlist.txt` + `rockyou.txt` for dictionary attacks (lab only).
- Dictionary attack simulator (SHA-256 demo).
- Password strength analyzer using zxcvbn.
- Password policy checker (Strong / Medium / Weak).
- CSV report generation for audit results.

## Installation

```bash
git clone https://github.com/bsinghceh-design/password-policy-testing-toolkit.git
cd password-policy-testing-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python cli.py
