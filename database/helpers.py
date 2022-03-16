def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }

def state_count_helper(state_count) -> dict:
    return {
        "id": str(state_count['_id']),
        "date": state_count['date'],
        "state": state_count["state"],
        "ad_count": state_count["ad_count"],
        "avg_age": state_count["avg_age"],
        "email_count": state_count["email_count"],
        "phone_count": state_count["phone_count"]
    }

def city_count_helper(city_count) -> dict:
    return {
        "id": str(city_count['_id']),
        "date": city_count['date'],
        "city": city_count["city"],
        "ad_count": city_count["ad_count"],
        "avg_age": city_count["avg_age"],
        "email_count": city_count["email_count"],
        "phone_count": city_count["phone_count"]
    }