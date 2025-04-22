# src/promote.py

import shutil
import os

src = "models/staging/house_price_model.pkl"
dst = "models/prod/house_price_model.pkl"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("✅ Model promoted from staging to production.")
else:
    raise FileNotFoundError("🚫 Staging model not found.")
