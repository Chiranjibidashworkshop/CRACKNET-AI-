import numpy as np
import string

def extract_features(password):
    if len(password) == 0:
        return {
            'length': 0,
            'digits': 0,
            'upper': 0,
            'lower': 0,
            'special': 0,
            'entropy': 0
        }

    prob = [password.count(c) / len(password) for c in set(password)]
    entropy = -sum(p * np.log2(p) for p in prob)

    return {
        'length': len(password),
        'digits': sum(c.isdigit() for c in password),
        'upper': sum(c.isupper() for c in password),
        'lower': sum(c.islower() for c in password),
        'special': sum(c in string.punctuation for c in password),
        'entropy': entropy
    }