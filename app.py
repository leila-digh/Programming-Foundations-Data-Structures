# Sets are mutable
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits.update(["mango", "grape"])
print(fruits)

# remove(item) - can raise KeyError
# discard(item) - does not raise KeyError

fruits.remove("banana")
fruits.discard("tomato")
print(fruits)