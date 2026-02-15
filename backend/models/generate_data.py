import pandas as pd
import random

num_records = 1000

departments = ["ER", "OPD", "Radiology"]

data = []

for _ in range(num_records):
    department = random.choice(departments)
    hour = random.randint(0, 23)
    day_of_week = random.randint(0, 6)  # 0=Mon, 6=Sun
    doctors_available = random.randint(1, 5)
    severity = random.randint(1, 5)

    # Simulate queue size based on department + time
    base_queue = {
        "ER": random.randint(10, 30),
        "OPD": random.randint(3, 15),
        "Radiology": random.randint(5, 20)
    }[department]

    # Peak hour effect
    if 9 <= hour <= 12 or 17 <= hour <= 20:
        base_queue += random.randint(5, 15)

    patients_in_queue = max(0, base_queue)

    # Wait time logic
    load_factor = patients_in_queue / doctors_available
    wait_time = load_factor * random.randint(5, 10)

    # Severity reduces wait time (priority treatment)
    wait_time *= (1 - severity * 0.08)

    wait_time = max(1, round(wait_time, 1))

    data.append([
        department,
        hour,
        day_of_week,
        doctors_available,
        patients_in_queue,
        severity,
        wait_time
    ])

df = pd.DataFrame(data, columns=[
    "department",
    "hour_of_day",
    "day_of_week",
    "doctors_available",
    "patients_in_queue",
    "severity_level",
    "wait_time"
])

df.to_csv("hospital_queue_data.csv", index=False)

print("Dataset generated: hospital_queue_data.csv")
print("Total records:", len(df))
