employee_salaries = {"Alice": 50000, "Bob": 60000}

# print(employee_salaries["Charlie"])
#key error

#avoiding key errors
#get
# print(employee_salaries.get("Charlie", "Not Found"))

try:
  print(employee_salaries["Charlie"])
except KeyError:
  print("Not Found")