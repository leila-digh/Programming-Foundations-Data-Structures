# 1, 10, 11, 100, 101, 110, 111, 1000
from collections import deque

def generate_binary(n):
    # Your code goes here
    result = []
    if n <= 0:
        return []
    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        result.append(binary)
        queue.append(binary*10)
        queue.append(binary*10 + 1)
    return result
