fruits = {"apple", "banana", "cherry"}
# print(fruits)

fruits.add("orange")
# print(fruits)

fruits.update(["mango", "grape"])
# print(fruits)

#remove

fruits.remove("banana")
print(fruits)

# try:
#   fruits.remove("tomato")
# except KeyError:
#   print("Not in Set")

#discard
fruits.discard("tomato")
print(fruits)
