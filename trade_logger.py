import csv, os
from datetime import datetime
from config import TRADE_LOG_FILE

def log_trade(data):
    exists = os.path.exists(TRADE_LOG_FILE)
    with open(TRADE_LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not exists:
            writer.writeheader()
        writer.writerow(data | {"time": datetime.now()})
