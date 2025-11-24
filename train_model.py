import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# Load dataset
df = pd.read_csv("UPI_Fraud_Dataset.csv")

# Encode categorical features (TransactionType, DeviceType)
le1 = LabelEncoder()
df['TransactionType'] = le1.fit_transform(df['TransactionType'])

le2 = LabelEncoder()
df['DeviceType'] = le2.fit_transform(df['DeviceType'])

# Features (X) and target (y)
X = df.drop(columns=['TransactionID','IsFraud'])
y = df['IsFraud']

# Split dataset into Train & Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ======================
# Train Random Forest
# ======================
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

print("🔹 Random Forest Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Save model
joblib.dump(rf_model, "rf_model.pkl")

# ======================
# Train Logistic Regression
# ======================
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

print("\n🔹 Logistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print(confusion_matrix(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

# Save model
joblib.dump(log_model, "log_model.pkl")

print("\n✅ Models trained and saved successfully!")