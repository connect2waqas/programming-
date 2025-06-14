# Key outline:
# properties of set
# boolean values in set
# nesting is not the property fo the set
# checking items in the set


# BOOLEAN VALUE:

# set consider 1 and true same and 0 and False is same:

# my_set = {"animal","plants",1,2,3,4,5,0, True,False}

# print(my_set) # here set consider the 1 and true is same and 0 and false is same

# anothe_set = {True,0,False,1}
# print(anothe_set) # here it ignore the 1 and select the True as 1
#  NESTING IS NOT A PROPERTY OF A SET:

# a = {{1,2,3,4,5},{4,3,2,1},{3,5,6,7,8,9}}

# print(a) it rises to error becuase the nesting is not property of set

# CHECKING IF ITEMS IS PRESENT IN A SET: USING THE KEYWORD 'IN':

# a = {"data","science","swati"}

# print("science" and "swati" in a)

# print("data" in a) 

# b = {"movie","ayoub","sham"}

# print("sham" in b)

# FINDING THE LENGTH OF THE SET:

# mix_set = {1,2,3,4,5,6,"waqas","Ai engineer",True}

# print(len(mix_set))

# length = 0

# for i in mix_set:
#     length +=1
# # print(f"The length of the set is {length}")
# print(length) # finding length through other than len() method okay

#  ITEMS ADDING TO A SET:
# we cannot change any item in a set but we can adding any items to it.

# a = {'a1','b1','c1',1,2,3}
# a.add("d1")
# print(a)

# update method : joining different set:

a = {1,2,3,4}
b = {6,8,5,7}

# a.update(b)
# print(a)
# concatenation is not allowed for set okay

# a.update(b)
# print(a,'\n',type(a))

# b.update(a)
# print(b,'\n',type(b))
# c = a.union(b)
# print(c) # it also combine the set and can be return only when assine it to anothter variable okay

# code = {'data','python','code'}

# code1 = {1,2,3,4,5,6,7,"deep learning"}

#  code.update(code1)

# print(code)
# code2 = code.union(code1) # in union we have to assigne the code to a variable for getting result.

# print(code)

# ROMOVING ELEMENT FROM THE LIST:

# data = {"data","science","deep learning",20,10,30,40,50,1.4,4.5,3.14}
# print(data.remove(40))
# newdata=data.remove(40)
# print(newdata)
# print(data)
# data.remove("data")
# print(data)
# the remove is used to remove the value with your interest

# POP() METHOD IN PYTHON 
#In this method we can remove the element without our interest. it can remove the value randomly okay and they return the remove value okay


# data = {"data","science","deep learning",20,10,30,40,50,1.4,4.5,3.14}

# c = data.pop()
# print(data,'\n',c)

# data = {"data","science","deep learning",20,10,30,40,50,1.4,4.5,3.14}

# data.clear()

# print(data)

# data = {"data","science","deep learning",20,10,30,40,50,1.4,4.5,3.14}

# del data

# print(data) # here it delete all the set 
