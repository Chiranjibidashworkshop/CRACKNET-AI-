import sys
import os

sys.path.append(os.path.abspath("src/features"))

from feature_engineering import extract_features

password = "P@ssword123"

features = extract_features(password)

print("Password:", password)
print("Extracted Features:", features)
