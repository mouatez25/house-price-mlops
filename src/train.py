
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    df = pd.read_csv("data/house_price_data.csv")
    X = df.drop("price", axis=1)
    y = df["price"]
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/dev/house_price_model.pkl")
    print("Model trained and saved to dev.")

if __name__ == "__main__":
    train_model()
