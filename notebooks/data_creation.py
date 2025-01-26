import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    "timestamp": pd.date_range(start="2025-01-01", periods=1000, freq="H"),
    "cpu_usage": np.random.randint(20, 100, size=1000),
    "memory_usage": np.random.randint(30, 90, size=1000),
    "errors": np.random.randint(0, 10, size=1000),
    "device_status": np.random.choice([0, 1], size=1000, p=[0.9, 0.1])
}
df = pd.DataFrame(data)
df.to_csv("data/processed/network_logs.csv", index=False)
print("Synthetic data created and saved to data/processed/network_logs.csv")
