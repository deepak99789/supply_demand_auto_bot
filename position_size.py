def position_size(equity, risk_pct, entry, sl):
    risk_amt = equity * (risk_pct / 100)
    risk_per_unit = abs(entry - sl)
    if risk_per_unit == 0:
        return 0
    return round(risk_amt / risk_per_unit, 2)
