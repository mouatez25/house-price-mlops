import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
from datetime import datetime
import os

def train_model():
    df = pd.read_csv("data/house_price_data.csv")
    X = df.drop("price", axis=1)
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    os.makedirs("models/dev", exist_ok=True)
    joblib.dump(model, "models/dev/house_price_model.pkl")

    # Logging
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | TRAIN | model=RandomForestRegressor | MAE={mae:.2f} | saved=dev\n"

    with open("logs/train_log.txt", "a") as f:
        f.write(log_entry)

    print("✅ Model trained and saved to dev.")
    print(log_entry.strip())

if __name__ == "__main__":
    train_model()
