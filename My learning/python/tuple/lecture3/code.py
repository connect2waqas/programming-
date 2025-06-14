# THIS IS LECTURE NO 3 OF TUPLE
# CONVERTING TUPLE IN TO LIST
# ADDING THE TUPLE
# CHANGING ITEMS
# REMOVING ITEMS
# JOINING THE TUPLE
# DELETING THE TUPLE
# MULTIPLAYING TUPLE
# PRACTICE QUESTIONS

# once we have created the tuple then we cannot remove ,
#  adding , and changes its value . but we have a way 
# that convert the tuple into list and then tuple can
# can be change , add , remove and modified.

# xyz = ("data","science","swati","artifial","intelligence")

# print(xyz,"\n" ,type(xyz)) 

# here we have to convert the tuple into list:

# zyx = list(xyz)

# print(zyx, "\n", type(zyx))
# zyx.append("cybersecruity")
# print(zyx) # after that we have to convert this list into tuple again okay

# zyx_to_tuple = tuple(zyx)
# print(zyx_to_tuple,"\n",type(zyx_to_tuple)) # this is so amazing sir 

# xyz = ("data","science","swati","artifial","intelligence")

# zyx = ("machine learning","deep learning","Genrative AI")

# # ADDING TUPLE TO A TUPLE

# xyz += zyx

# print(xyz)
# print(len(xyz))

#  REMOVING THE ITEMS FROM THE TUPLE

# friuts = ("apple","banana","cheery","date") # we have to first convert to the list and remove the items

# friuts_to_list = list(friuts)

# friuts_to_list.remove("date")

# print(friuts_to_list, "\n", type(friuts_to_list))

# list_to_tuple = tuple(friuts_to_list)
# print(list_to_tuple, "\n",type(list_to_tuple))

# friuts = ("apple","banana","cheery","date")

# friuts_to_list = list(friuts)
# print(friuts_to_list,"\n", type(friuts_to_list))

# friuts_to_list[3] ="mango"

# print(friuts_to_list)

# friuts_to_list[0] = "cocunut"

# print(friuts_to_list)

# print(tuple(friuts_to_list))

#  DEL KEYWORDS USAGE

# matrix = ((1, 2), (3, 4), (5, 6))
# print(matrix[1][0])  # 3 → Accessing nested elements

# matrix = ((1,2),(3,4),(5,6))

# # print(matrix[0][0]) # working with nested tuple
# sorted(matrix)
# print(matrix[1][0],matrix[1][1],matrix[2][0],matrix[2][1],matrix[0][0],matrix[0][1])


# T = (1,2,3,4,5)
# del T
# print(T) # this delete entirely the tuple from the memory okay

# ADDING TWO TUPPLE

# a = ('a','b','c')
# b = (1 , 2, 3 )

# c = a + b

# print(c, "\n",type(c))

# MULTIPLICATION OF THE TUPLE

friuts = ('apple','banana','cheery','mango')

# for i in friuts:
#     print(i * 2) # not best practice 
# print(friuts)

tup1 = friuts * 2

print(tup1)
print(sorted(tup1))