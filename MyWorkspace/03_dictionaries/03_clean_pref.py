
def clean_preferences(user_pref):
    # Your code goes here
    # to_delete = []
    new_dict = {}
    # for key, value in new_dict.items():
    #     if(value == None):
    #         print(f"{key}: {value}")
    #         to_delete.append(key)

    # for key in to_delete:
    #     del new_dict[key]

    for key, value in user_pref.items():
        if value is not None:
            new_dict[key] = value

    return new_dict
