my_list = [1, 7, 3]

print(sorted(my_list, reverse=True))

student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]

print(sorted(student_grades, key=lambda x: x[1], reverse=True))

#number of comparisions depends on sorting algorithm