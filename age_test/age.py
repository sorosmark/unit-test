def categorise_by_age(age):
    if 0 <= age <= 9:
        return "child"
    if 10 <= age <= 18:
        return "teenager"
    if 19 <= age <= 65:
        return "adult"
    if 66 <= age <= 90:
        return "old"
    if 91 <= age <= 120:
        return "halfdead"
    else:
        return f"this is not a valid age: {age}"