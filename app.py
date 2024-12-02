my_list = [8, 5, 0, 3, 9, 7]
item = 7

def search(search_element):
  for element in my_list:
    if element == search_element:
      return True
  return False

print(search(item))

# Linear Search (Sequential Search)
# - Best case: First item
# - Worst case: Not in list
# - Linear time algorithm: O(n)

item_index = my_list.index(item)

# The more information we have about our data the more we can optimize the searching algorithm

# Searching and sorting both take time