# tuples
# immutable;
# ideal for coordinates and rbg values

# point = (5, 2)

# x = point[0]
# y = point[1]

# print(x)
# print(y)

# function that returns area and perimter of a square


def calculate_square_properties(side_length):
    area = side_length**2
    perimeter = 4*side_length
    return (area, perimeter)


result = calculate_square_properties(5)
print(f"Area = {result[0]}")
print(f"Perimeter = {result[1]}")
