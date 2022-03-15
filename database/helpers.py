def student_helper(student) -> dict:
    return {
        "id": str(student['_id']),
        "fullname": student['fullname'],
        "email": student['email'],
        "course_of_study": student['course_of_study'],
        "year": student['year'],
        "GPA": student['gpa']
    }

def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }

def city_ad_helper(city_ad) -> dict:
    return {
        'city': str(city_ad['city']),
        'ads': int(city_ad['ads']),
        'date_from': str(city_ad['date_from']),
        'date_to': str(city_ad['date_to']),
    }

def state_ad_helper(state_ad) -> dict:
    return {
        'state': str(state_ad['state']),
        'ads': int(state_ad['ads']),
        'date_from': str(state_ad['date_from']),
        'date_to': str(state_ad['date_to']),
    }

def city_phone_helper(city_phone) -> dict:
    return {
        'city': str(city_phone['city']),
        'phones': int(city_phone['phones']),
        'date_from': str(city_phone['date_from']),
        'date_to': str(city_phone['date_to']),
    }

def state_phone_helper(state_phone) -> dict:
    return {
        'state': str(state_phone['state']),
        'phones': int(state_phone['phones']),
        'date_from': str(state_phone['date_from']),
        'date_to': str(state_phone['date_to']),
    }

def city_email_helper(city_email) -> dict:
    return {
        'city': str(city_email['city']),
        'emails': int(city_email['emails']),
        'date_from': str(city_email['date_from']),
        'date_to': str(city_email['date_to']),
    }

def state_email_helper(state_email) -> dict:
    return {
        'state': str(state_email['state']),
        'emails': int(state_email['emails']),
        'date_from': str(state_email['date_from']),
        'date_to': str(state_email['date_to']),
    }

def city_count_helper(city_count) -> dict:
    return {
        'city': str(city_count['city']),
        'date': str(city_count['date']),
        'ad_count': int(city_count['ad_count']),
        'avg_age': float(city_count['avg_age']),
        'email_count': int(city_count['email_count']),
        'phone_count': int(city_count['phone_count']),
    }