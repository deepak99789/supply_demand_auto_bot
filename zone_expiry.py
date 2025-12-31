def is_zone_expired(current, created, limit):
    return (current - created) > limit
