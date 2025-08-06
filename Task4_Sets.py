set_one = input("Enter elements for set one (comma-separated): ")
set_one = set(set_one.split(","))

set_two = input("Enter elements for set two (comma-separated): ")
set_two = set(set_two.split(","))

# Find the union of both sets
union_set = set_one | set_two
print("Union of both sets:", union_set)

# Find the intersection of both sets
intersection_set = set_one & set_two
print("Intersection of both sets:", intersection_set)

# Find the difference of both sets
difference_set = set_one - set_two
print("Difference of set one from set two:", difference_set)
