user_preferences = {
    "language": "English",
    "fontSize": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enableLocation": False,
    "volumeLevel": 80,
    "dateFormat": "MM/DD/YYYY"
}

user_preferences["language"] = "Spanish"
user_preferences["volumeLevel"] = 50

user_preferences["highlightColor"] = "yellow"

#del user_preferences["currency"]
removed_item = user_preferences.pop("currency", "N/A")

print(user_preferences)


