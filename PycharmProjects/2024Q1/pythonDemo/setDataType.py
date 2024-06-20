sets = {1, 2, 3, 4, 5, 5, 5, 10}
print(sets)

lst1 = [5, 1, 6, 4, 10, 9]
set1 = {5, 1, 6, 4, 10, 9}
print(lst1)
print(set1)

set1.remove(10)
print(set1)

new_set = {17, 20}
set1.update(new_set)
print(set1)

amirs_set = {1, 2, 3, 4, 5}
gonca_set = {1, 2, 6, 7, 8}

print(amirs_set.difference(gonca_set))
print(gonca_set.difference(amirs_set))

