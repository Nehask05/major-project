import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('UPI_Fraud_Dataset.csv')

# Show first 5 rows
print("🔹 First 5 rows of dataset:")
print(df.head())

# Show dataset info
print("\n🔹 Dataset Info:")
print(df.info())

# Show summary statistics
print("\n🔹 Statistical Summary:")
print(df.describe())

# Count Fraud vs Legitimate
print("\n🔹 Fraud vs Legitimate count:")
print(df['IsFraud'].value_counts())

# =======================
# 📊 Visualizations
# =======================

# Fraud vs Legitimate (bar chart)
plt.figure(figsize=(5,4))
sns.countplot(x='IsFraud', data=df, palette='Set2')
plt.title("Fraud vs Legitimate Transactions")
plt.xlabel("0 = Legitimate, 1 = Fraud")
plt.ylabel("Count")
plt.show()

# Transaction Amount Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount (INR)")
plt.ylabel("Frequency")
plt.show()

# Fraud based on Transaction Type
plt.figure(figsize=(6,4))
sns.countplot(x='TransactionType', hue='IsFraud', data=df, palette='Set1')
plt.title("Fraud Distribution by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.show()

# Fraud based on Device Type
plt.figure(figsize=(6,4))
sns.countplot(x='DeviceType', hue='IsFraud', data=df, palette='Set3')
plt.title("Fraud Distribution by Device Type")
plt.xlabel("Device Type")
plt.ylabel("Count")
plt.show()