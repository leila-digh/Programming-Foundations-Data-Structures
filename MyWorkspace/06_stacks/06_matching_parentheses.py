from collections import deque

def check_matching_parentheses(s):
    # Your code goes here
    new_stack = deque()
    for char in s:
        if char == "(":
            new_stack.append(char)
        elif char == ")":
            if not new_stack:
                return False
            new_stack.pop()
        print(new_stack)
    return len(new_stack) == 0
