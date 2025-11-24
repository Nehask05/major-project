import pandas as pd
import random
from faker import Faker

# Initialize Faker (for generating fake but realistic data)
fake = Faker()
data = []

for i in range(1, 1001):  # 1000 transactions
    # Transaction details
    amount = round(random.uniform(10, 100000), 2)  # Amount between 10 and 1 lakh
    transaction_type = random.choice(['P2P','Merchant','Bill'])
    device_type = random.choice(['Mobile','Web','POS'])
    transaction_hour = random.randint(0,23)
    is_new_device = random.choice([0,1])  # 0 = old device, 1 = new device
    is_international = random.choices([0,1], weights=[0.95,0.05])[0]
    daily_count = random.randint(1,7)  # How many transactions that day
    previous_fraud = random.choices([0,1], weights=[0.9,0.1])[0]

    # Fraud logic (risk scoring)
    risk_score = 0
    if amount > 50000: risk_score += 2
    if transaction_hour in [2,3,4,5]: risk_score += 1
    if is_new_device: risk_score += 1
    if is_international: risk_score += 2
    if daily_count > 5: risk_score += 1
    if previous_fraud: risk_score += 2

    # Final fraud decision
    is_fraud = 1 if risk_score >= 4 or random.random() < 0.03 else 0

    data.append([i, amount, transaction_type, device_type, transaction_hour,
                 is_new_device, is_international, daily_count, previous_fraud, is_fraud])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'TransactionID','Amount','TransactionType','DeviceType',
    'TransactionHour','IsNewDevice','IsInternational',
    'DailyTransactionCount','PreviousFraudFlag','IsFraud'
])

# Save dataset
df.to_csv('UPI_Fraud_Dataset.csv', index=False)
print("✅ Dataset with 1000 entries created successfully!")