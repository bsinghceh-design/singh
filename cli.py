
# cli.py

from dictionary_generator import generate_dictionary
from brute_force_simulator import simulate_dictionary_attack
from password_analyzer import analyze_password
from report_generator import generate_csv_report
from password_policy_checker import check_password_policy
import hashlib

def main_menu():
    print("=== Password Policy Testing Toolkit ===")
    print("1. Generate dictionary")
    print("2. Simulate dictionary attack (demo)")
    print("3. Analyze single password (entropy/zxcvbn)")
    print("4. Check password policy (Strong/Medium/Weak)")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        words = input("Enter base words (comma separated): ")
        base_words = [w.strip() for w in words.split(",") if w.strip()]
        outfile = generate_dictionary(base_words)
        print(f"[+] Wordlist generated: {outfile}")

    elif choice == "2":
        target_pw = input("Enter demo password to hash (e.g., admin123): ")
        hash_val = hashlib.sha256(target_pw.encode()).hexdigest()
        print(f"[i] Target SHA-256 hash: {hash_val}")
        result = simulate_dictionary_attack(hash_val)
        print(result)

    elif choice == "3":
        pw = input("Enter password to analyze (zxcvbn): ")
        result = analyze_password(pw)
        print(result)
        generate_csv_report([result])

    elif choice == "4":
        pw = input("Enter password to check policy: ")
        result = check_password_policy(pw)
        print(f"Status: {result['status']}")
        if result["reasons"]:
            print("Details:")
            for r in result["reasons"]:
                print(" -", r)

    else:
        print("Bye!")


if __name__ == "__main__":
    main_menu()

