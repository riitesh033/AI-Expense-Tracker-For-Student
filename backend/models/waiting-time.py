import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Example hospital data
data = {
    "department": ["ER", "ER", "OPD", "Radiology", "OPD", "ER"],
    "patients_in_queue": [20, 15, 5, 10, 3, 25],
    "doctors_available": [2, 3, 2, 1, 2, 2],
    "severity_level": [4, 3, 2, 5, 1, 5],
    "wait_time": [40, 25, 10, 50, 5, 60]
}

df = pd.DataFrame(data)

# Convert text to numbers
df = pd.get_dummies(df, columns=["department"])

X = df.drop("wait_time", axis=1)
y = df["wait_time"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

print("Model trained!")

# Predict for new patient
new_patient = pd.DataFrame({
    "patients_in_queue": [18],
    "doctors_available": [2],
    "severity_level": [4],
    "department_ER": [1],
    "department_OPD": [0],
    "department_Radiology": [0]
})

prediction = model.predict(new_patient)
print("Predicted wait time:", prediction[0], "minutes")
