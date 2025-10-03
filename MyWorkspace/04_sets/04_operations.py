set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

# union; combination w no duplicates
union_set = set_A.union(set_B)
print(f"Union == {union_set} \n")

intersection_set = set_A.intersection(set_B)
print(f"Intersection == {union_set}\n")

#in set a but not in set B
difference_set = set_A.difference(set_B)
print(f"Set A - Set B == {difference_set}")

#in set b but not in set A
difference_set_BA = set_B.difference(set_A)
print(f"Set B - Set A == {difference_set_BA}")

#elements unique to both, union of the differences
symmetric_difference_set = set_A.symmetric_difference(set_B)
print(f"Symmetric difference of set A and set B = {symmetric_difference_set}")
