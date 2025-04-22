import shutil
import os
from datetime import datetime

def promote_dev_to_staging():
    src = "models/dev/house_price_model.pkl"
    dst = "models/staging/house_price_model.pkl"

    if not os.path.exists(src):
        raise FileNotFoundError("🚫 Dev model not found. Cannot promote.")

    os.makedirs("models/staging", exist_ok=True)
    shutil.copy(src, dst)

    # Log the promotion
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/promotion_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} | PROMOTE: dev → staging | ✅ Success\n")

    print("✅ Model promoted from dev to staging.")

if __name__ == "__main__":
    promote_dev_to_staging()
