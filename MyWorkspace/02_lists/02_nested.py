seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]
# get lauren
print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        # print(f"Row: {i+1}, Students: {row}")
        print(f"{student_name:10} is in row {i+1}, seat {j+1}")
