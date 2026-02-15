import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

print("Starting model...")

# 1️⃣ Load CSV safely
df = pd.read_csv("hospital_queue_data.csv", encoding='utf-8-sig')
df.columns = df.columns.str.strip()  # remove extra spaces / BOM

# 2️⃣ Convert department text → dummy columns
df = pd.get_dummies(df, columns=["department"])

# 3️⃣ Define features and target
X = df.drop("wait_time", axis=1)
y = df["wait_time"]

# 4️⃣ Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

print("Model trained!")

# 6️⃣ Test model
predictions = model.predict(X_test)
print("Actual wait times:", list(y_test))
print("Predicted wait times:", list(predictions))

error = mean_absolute_error(y_test, predictions)
print("Average prediction error:", error, "minutes")

# 7️⃣ Predict for a new patient
# Example: new patient
new_patient_data = {
    "hour_of_day": [10],
    "day_of_week": [2],
    "doctors_available": [2],
    "patients_in_queue": [18],
    "severity_level": [4],
    "department_ER": [1],
    "department_OPD": [0],
    "department_Radiology": [0]
}

# Convert to DataFrame with columns in the same order as training
new_patient = pd.DataFrame(new_patient_data)
new_patient = new_patient[X.columns]  # ensures order matches

prediction = model.predict(new_patient)
print("Predicted wait time for new patient:", prediction[0], "minutes")
