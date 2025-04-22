
import pandas as pd
from sklearn.metrics import mean_absolute_error
import joblib

def validate_model(threshold=30000):
    df = pd.read_csv("data/house_price_data.csv")
    X = df.drop("price", axis=1)
    y = df["price"]

    model = joblib.load("models/dev/house_price_model.pkl")
    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)

    assert mae < threshold, f"Validation failed: MAE {mae}"
    print(f"Validation passed: MAE = {mae}")

if __name__ == "__main__":
    validate_model()
