def calculate_rr(entry, sl, target):
    risk = abs(entry - sl)
    reward = abs(target - entry)
    if risk == 0:
        return 0
    return round(reward / risk, 2)
