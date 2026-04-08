import pandas as pd
import os
import sys

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from features.feature_engineering import extract_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
# Load dataset (LIMIT SIZE FOR SPEED)
df = pd.read_csv("data/processed/cleaned_passwords.csv", nrows=50000)

# Ensure correct column name
df.columns = ['password']

print("Dataset loaded:", len(df))

# Labeling function
def label_password(pwd):
    pwd = str(pwd)
    length = len(pwd)

    if length < 6:
        return "Weak"
    elif length < 10:
        return "Medium"
    else:
        return "Strong"

# Feature extraction
feature_data = []

for pwd in df['password']:
    f = extract_features(pwd)
    f['label'] = label_password(pwd)
    feature_data.append(f)

data = pd.DataFrame(feature_data)

print("Feature extraction done")

# Split data
X = data.drop('label', axis=1)
y = data['label']

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print("Model training completed")

# Evaluation
y_pred = model.predict(X_test)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/password_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("\nModel saved successfully!")