import string

# Speed assumptions
BRUTEFORCE_SPEED = 1e6   # 1 million guesses/sec
AI_SPEED = 1e9           # 1 billion guesses/sec


def calculate_charset(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32

    return charset


def calculate_search_space(password):
    charset = calculate_charset(password)
    return charset ** len(password)


def time_to_crack(password):
    space = calculate_search_space(password)

    brute_time = space / BRUTEFORCE_SPEED
    ai_time = space / AI_SPEED

    return brute_time, ai_time


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"