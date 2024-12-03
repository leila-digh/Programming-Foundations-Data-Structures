set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
print("Union of set A and set B: ", union_set)

intersection_set = set_A.intersection(set_B)
print("Intersection of set A and set B: ", intersection_set)

difference_set = set_A.difference(set_B)
print("Set A - Set B: ", difference_set)

difference_set_BA = set_B.difference(set_A)
print("Set B - Set A: ", difference_set_BA)

symmetric_difference_set = set_A.symmetric_difference(set_B)
print("Symmetric difference of set A and set B: ", symmetric_difference_set)