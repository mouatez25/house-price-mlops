# src/promote.py

import shutil
import os
from datetime import datetime

def promote_staging_to_prod():
    src = "models/staging/house_price_model.pkl"
    dst = "models/prod/house_price_model.pkl"

    if not os.path.exists(src):
        raise FileNotFoundError("🚫 Staging model not found.")

    os.makedirs("models/prod", exist_ok=True)
    shutil.copy(src, dst)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("logs", exist_ok=True)
    with open("logs/promotion_log.txt", "a") as f:
        f.write(f"{timestamp} | PROMOTE: staging → prod | ✅ Success\n")

    print("✅ Model promoted from staging to production.")

if __name__ == "__main__":
    promote_staging_to_prod()
