# password_analyzer.py

from zxcvbn import zxcvbn

def analyze_password(password):
    """
    Uses zxcvbn to estimate password strength.
    """
    result = zxcvbn(password)
    score = result["score"]          # 0–4
    crack_time = result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    feedback = result["feedback"]["suggestions"]
    return {
        "password": password,
        "score": score,
        "crack_time": crack_time,
        "feedback": feedback,
    }


if __name__ == "__main__":
    print(analyze_password("Password@123"))
