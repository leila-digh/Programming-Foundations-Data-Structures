# Problem Statement: Compute the average number of books each student has read this year

student_books_list = [5, 3, 0, 7, 2, 4, 6, 8, 1, 3, 9, 5, 2, 6, 7, 4]

# print(f"There are {num_of_students} students in the class")
print(student_books_list)


# First student read 3 more books
student_books_list[0] += 3
# Second student read 1 more book
student_books_list[1] += 1
# Last student read 2 more books
student_books_list[-1] += 2

student_books_list.append(3)
student_books_list.append(5)

print(student_books_list)

num_of_students = len(student_books_list)

# # sum/ num
total_books_sum = 0

for books in student_books_list:
    total_books_sum += books

print(f"There are {total_books_sum} books read in total in the class")

average_books_read = total_books_sum/num_of_students
print(f"On average, each student read {average_books_read:.2f} books")
