# dictionary_generator.py

def generate_dictionary(base_words, output_file="wordlist.txt"):
    """
    Very simple dictionary generator.
    Takes a list of base words and creates small mutated wordlist.
    """
    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())
        # simple number appends
        for n in ["1", "123", "2024", "2025"]:
            wordlist.add(word + n)
        # simple leet-style
        wordlist.add(word.replace("a", "@").replace("o", "0").replace("e", "3"))

    with open(output_file, "w") as f:
        for w in sorted(wordlist):
            f.write(w + "\n")

    return output_file


if __name__ == "__main__":
    # quick test
    generate_dictionary(["admin", "password"])
    print("[+] wordlist.txt generated")
