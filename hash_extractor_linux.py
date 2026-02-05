# hash_extractor_linux.py

def extract_linux_hashes(shadow_file_path="shadow_demo.txt", output_file="hashes.txt"):
    """
    Reads a copy of /etc/shadow (lab only!) and extracts user:hash lines.
    You must copy /etc/shadow to shadow_demo.txt using sudo (in lab).
    """
    hashes = []

    try:
        with open(shadow_file_path, "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) >= 2:
                    user = parts[0]
                    pw_field = parts[1]
                    if pw_field not in ["*", "!", "x", ""]:
                        hashes.append(f"{user}:{pw_field}")
    except FileNotFoundError:
        print(f"[!] File not found: {shadow_file_path}")
        return None

    with open(output_file, "w") as f:
        for h in hashes:
            f.write(h + "\n")

    print(f"[+] Extracted {len(hashes)} hashes to {output_file}")
    return output_file


if __name__ == "__main__":
    extract_linux_hashes()
