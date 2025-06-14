# In this part of tuple we will disscus the following topics:
# indexing in tuple
# positive indexing
# negative indexing
# slicing
# positive slicing
# negative slicing
# reversing the tuple
# properties of tuple
# methods of tuple
# count method
# index method

# LETS DO THIS STEP BY STEP:

# indexing
# positve indexing

# my_tuple = (10,20,30,40,50)
# print(my_tuple[0],my_tuple[1],my_tuple[2],my_tuple[3],my_tuple[4])
# print(my_tuple[1])
# print(my_tuple[2])
# print(my_tuple[3])
# print(my_tuple[4])


# NEGATIVE INDEXING

# my_tuple = (10,20,30,40,50)

# print(my_tuple[-1])
# print(my_tuple[-2])
# print(my_tuple[-3])
# print(my_tuple[-4])
# print(my_tuple[-5])
# print(my_tuple[-1],my_tuple[-2],my_tuple[-3],my_tuple[-4],my_tuple[-5])

# SLICING IN TUPLE 
# Same like the list slicing

# alph = ("a","b","c","d","e")
# print((alph[1:4],alph[:],alph[0:3],alph[0:]))  
# The last one is alway ignore in python. we 
# have to write n+1 to get best result okay

# print(list(alph))

# alph = ("a","b","c","d","e")

# SLICING WITH JUMPING

# print(alph[::2]) # Jump by one step okay
# print(alph[::3]) # Jump by two step okay
# print(alph[::4]) # Jump by three step okay
# print(alph[::2],alph[::3],alph[::4])

# #  SLICING WITH NEGATIVE INDEXING
# print(alph[::-1]) # it always return
#  tuple in reverse order ('e', 'd', 'c', 'b', 'a')
# print(alph[2::-1]) # Negativing slicing with 
# print(alph[3::-1]) # Negativing slicing 
# print(alph[4::-1]) # Negativing slicing 


# friut = ("apple","banana","cheery","date")

# print(friut[:-3]) # it says that start slicing from the 0 and stop on -3. is it clear sir.
# print(friut[-3:]) # it say that start from -3 and print so on in negative indexing
# print(friut[::-1]) # Reversing the whole tuple as a whole okay

# for i in friut: #just for fun okay
#     print(list(i[::-1]),end=" ")

# num = "1234"
# print(num.isdigit())

# string = "Hello"
# print(string.encode("utf-8"))
# print(string.translate({97:"x"}))

# T = (69,97,28,16,14,31,21,47)
# print(T[::]) # full tuple (69,97,28,16,14,31,21,47)
# print(T[3:]) # (16,14,31,21,47)
# print(T[:4:]) # (69,97,28,16)
# print(T[-2:-5])# ()

# DUPLICATE IS ALLOWED IN TUPLE 
# a = (12,13,14,15,16,17,15,11,12,18,19,20)
# print(a) # (12, 13, 14, 15, 16, 17, 15, 11, 12, 18, 19, 20)

# METHODS IN TUPLE :
# THERE ARE ONLY 2 METHODS IN TUPLE AND LESS DUE THE IMMUTABLITY OKAY

# COUNT METHOD: It is used to count the element in tuple like:

# T  = (12, 13, 14, 15, 16, 17, 15, 11, 12, 18, 19, 20)
# count = 0
# for i in T:
#     print(f"{i} : {T.count(i)}")
# USING LOOP TO ANSWER THE QUESTIONS:

# print(T.count(12))
# print(T.count(15))
# print(T.count(14))
# print(T.count(18))

# INDEX METHOD : It is used to returns first occurance of the element

# T = ("waqas","roman","ayush","swati","shahid","python")
# print(T.index("swati")) # it will return the first occurance of the index value
# print(T.index("shahid")) # return the index occurance

# for i in T:
#     print(f"{i} : {T.index(i)}")
