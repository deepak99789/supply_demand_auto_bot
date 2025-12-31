def is_fresh_zone(df, index, high, low):
    future = df.iloc[index+1:]
    for _, row in future.iterrows():
        if row["High"] >= low and row["Low"] <= high:
            return False
    return True
