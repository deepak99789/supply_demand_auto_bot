def classify_zone(pre, post):
    if pre == "RALLY" and post == "RALLY":
        return "RBR"
    if pre == "DROP" and post == "RALLY":
        return "DBR"
    if pre == "RALLY" and post == "DROP":
        return "RBD"
    if pre == "DROP" and post == "DROP":
        return "DBD"
    return None
