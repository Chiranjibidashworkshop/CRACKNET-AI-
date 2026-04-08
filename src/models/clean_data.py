import pandas as pd
import os

input_path = "data/raw/rockyou.txt"
output_path = "data/processed/cleaned_passwords.csv"

os.makedirs("data/processed", exist_ok=True)

passwords = []

print("Reading rockyou dataset...")

with open(input_path, "r", encoding="latin-1") as file:
    for line in file:
        pwd = line.strip()
        if pwd:
            passwords.append(pwd)

print("Total passwords loaded:", len(passwords))

df = pd.DataFrame(passwords, columns=["password"])

df.drop_duplicates(inplace=True)

print("After removing duplicates:", len(df))

df.to_csv(output_path, index=False)

print("✅ Cleaned dataset saved successfully!")
