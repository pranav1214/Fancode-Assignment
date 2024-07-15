def get_city(user):
    try:
        latitude = float(user["address"]["geo"]["lat"])
        longitude = float(user["address"]["geo"]["lng"])
        return -40 <= latitude <= 5 and 5 <= longitude <= 100
    except (TypeError, KeyError, ValueError):
        return False

def filter_users(users):
    return [user for user in users if get_city(user)]