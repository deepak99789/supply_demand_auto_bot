import yfinance as yf
from symbols import ALL_SYMBOLS
from timeframes import TIMEFRAMES
from zone_engine import classify_zone
from freshness import is_fresh_zone
from zone_expiry import is_zone_expired
from rr_calculator import calculate_rr
from position_size import position_size
from alert_tracker import is_duplicate
from telegram_alerts import send_alert
from config import *

def run():
    for symbol in ALL_SYMBOLS:
        for tf in TIMEFRAMES:
            df = yf.download(symbol, interval=tf, period="10d")
            if df.empty:
                continue

            df.reset_index(inplace=True)

            for i in range(5, len(df)-3):
                pre = "RALLY" if df.Close[i-2] > df.Open[i-2] else "DROP"
                post = "RALLY" if df.Close[i+2] > df.Open[i+2] else "DROP"

                zone = classify_zone(pre, post)
                if not zone:
                    continue

                high = df.High[i]
                low = df.Low[i]

                if not is_fresh_zone(df, i, high, low):
                    continue

                entry = low if zone in ["RBR","DBR"] else high
                sl = high if zone in ["RBR","DBR"] else low
                target = entry * (1.02 if zone in ["RBR","DBR"] else 0.98)

                rr = calculate_rr(entry, sl, target)
                if rr < 2:
                    continue

                qty = position_size(ACCOUNT_EQUITY, RISK_PERCENT, entry, sl)

                key = f"{symbol}{tf}{zone}{entry}"
                if is_duplicate(key):
                    continue

                msg = f"""
🔥 SUPPLY DEMAND ZONE

Symbol: {symbol}
TF: {tf}
Zone: {zone}
Entry: {round(entry,4)}
SL: {round(sl,4)}
RR: {rr}
Qty: {qty}
"""
                send_alert(msg)

if __name__ == "__main__":
    run()
