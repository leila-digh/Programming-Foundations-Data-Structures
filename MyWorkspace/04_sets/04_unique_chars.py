def has_unique_characters(s):
    # Your code goes here
    my_set = set(s)
    if len(my_set) == len(s):
        return True
    else:
        return False
