# report_generator.py

import pandas as pd

def generate_csv_report(results, output_file="audit_report.csv"):
    """
    Takes a list of dicts and saves them as CSV.
    Example result elements:
    {"password": "...", "score": 2, "crack_time": "...", "feedback": ["..."]}
    """
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"[+] Report saved to {output_file}")
    return output_file


if __name__ == "__main__":
    demo = [
        {"password": "admin123", "score": 0, "crack_time": "seconds", "feedback": ["too weak"]},
        {"password": "StrongPass@123", "score": 4, "crack_time": "centuries", "feedback": []},
    ]
    generate_csv_report(demo)
