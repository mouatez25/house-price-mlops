
import pandas as pd
from sklearn.metrics import mean_absolute_error
import joblib
from datetime import datetime
import os

def validate_model(threshold=30000, stage="dev"):
    df = pd.read_csv("data/house_price_data.csv")
    X = df.drop("price", axis=1)
    y = df["price"]

    model_path = f"models/{stage}/house_price_model.pkl"
    model = joblib.load(model_path)
    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)

    status = "PASS" if mae < threshold else "FAIL"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | Stage: {stage} | MAE: {mae:.2f} | Status: {status}\n"

    os.makedirs("logs", exist_ok=True)
    with open("logs/validation_log.txt", "a") as f:
        f.write(log_entry)

    print(log_entry.strip())
    assert mae < threshold, f"Validation failed: MAE = {mae}"

if __name__ == "__main__":
    validate_model()
