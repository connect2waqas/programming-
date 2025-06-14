# key outline :
# joining two set
# intersection of set
# union of set 
# maximume and minimum
# difference of set
# practice questions


set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)
set1.update(set2)
print(set3)
print(set1)

print(sum(set1.union(set2)))
print(max(set1.union(set2)))
print(min(set1.union(set2)))

# SET OPERATIONS

# INTERSECTION METHODE

# my_var = {52,32,23}
# another_var = {23,45,24}

# my_4 = my_var.intersection(another_var)
# print(my_4)  # they print common elements 

# my_5 = my_var.difference(another_var)
# print(my_5) # the print the difference in these set okay


# print(another_var.difference(my_var))

# students_passed_maths = {101,102,103,104,105}
# students_passed_science = {103,104,105,106,107}
# maths_science_passed = students_passed_maths.intersection(students_passed_science)
# maths_passed_only = students_passed_maths.difference(students_passed_science)
# science_passed_only = students_passed_science.difference(students_passed_maths)
# sub = students_passed_maths.issubset(students_passed_science)
# superset = students_passed_science.issuperset(students_passed_maths)
# print(f"Students who have passed both science and maths are: {maths_science_passed}")
# print(f'Total number of student passed both math and science are: {len(maths_science_passed)}')
# print(f"Student who have passed maths only are: {maths_passed_only}")
# print(f"Student who have passed science only are: {science_passed_only }")
# print(f"Is student passed maths is subset of science passed students: {sub}")
# print(f"Is student passed science is the superset of student passed maths: {superset}")