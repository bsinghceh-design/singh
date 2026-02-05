# brute_force_simulator.py

import hashlib
import time

def simulate_dictionary_attack(hash_to_crack, wordlist_file="wordlist.txt", algo="sha256"):
    """
    Simple dictionary attack simulation on a given hex hash.
    """
    start = time.time()
    attempts = 0

    try:
        with open(wordlist_file, "r") as f:
            for line in f:
                pw = line.strip()
                attempts += 1

                if algo == "sha256":
                    guess_hash = hashlib.sha256(pw.encode()).hexdigest()
                else:
                    guess_hash = hashlib.md5(pw.encode()).hexdigest()

                if guess_hash == hash_to_crack:
                    end = time.time()
                    return {
                        "cracked": True,
                        "password": pw,
                        "attempts": attempts,
                        "time_seconds": round(end - start, 3),
                    }
    except FileNotFoundError:
        print(f"[!] wordlist not found: {wordlist_file}")
        return None

    end = time.time()
    return {
        "cracked": False,
        "password": None,
        "attempts": attempts,
        "time_seconds": round(end - start, 3),
    }


if __name__ == "__main__":
    # quick demo: hash of "admin123"
    demo_hash = hashlib.sha256("admin123".encode()).hexdigest()
    result = simulate_dictionary_attack(demo_hash)
    print(result)
