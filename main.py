import re
import os
from zxcvbn import zxcvbn

def check_password_strength(password):
    print("\n--- Basic Checks ---")

    checks = {
        "Length >= 8": len(password) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Symbol": bool(re.search(r"[!@#$%^&*]", password)),
    }

    for check, passed in checks.items():
        print(f"{check}: {'✔' if passed else '✘'}")


def advanced_check(password):
    result = zxcvbn(password)

    print("\n--- Advanced Analysis ---")
    print("Score:", result['score'], "/ 4")

    print("\nSuggestions:")
    for s in result['feedback']['suggestions']:
        print("-", s)

def run_attack():
    print("\n--- Running Attack Simulation ---")

    # Reset previous cracked results
    os.system("rm -f ~/.john/john.pot")

    # Run attack
    os.system("john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt")

    # Show result
    os.system("john --show hash.txt")

# MAIN MENU
print("""
1. Check Password Strength
2. Run Attack Simulation
""")

choice = input("Select option: ")

if choice == "1":
    password = input("Enter password: ")
    check_password_strength(password)
    advanced_check(password)

elif choice == "2":
    run_attack()

else:
    print("Invalid option")
