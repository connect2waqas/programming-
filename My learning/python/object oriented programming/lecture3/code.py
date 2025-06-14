# INHERITANCE:
# Why is important in python for oops
# single inheritance
# multiple inheritance
# multilevel inheritance
# Hybrid inheritance
# Hierarichal inheritance
# Data curious minds
# practice questions
# it is process in which one class method are inherit by anthor class and use it.
# for the reason that reuse the code for many time...

# single inheritance:

# it is inheritance in which B class inherit the properties of class A.

# class parent:
#     def show(self):
#         print("This is parent class! ")

# class Child(parent):
#     def display(self):
#         print("This is child class! ")

# child = Child()

# child.show()
# child.display()

# Multiple inheritance:
# In multiple inheritance the child one inherit the properties of both parent A and B.

# class Mother:
#     def colur(self):
#         str1  = "it has white colur!"
#         print(str1)
# class Father:
#     def height(self):
#         str2 = "height is 5 feet!"
#         print(str2)

# class Child(Mother,Father):
#     def mix(self):
#         print("This is child of mother and father! ")

# child = Child()
# child.colur()
# child.height()
# child.mix()


# multilevel inheritance: 

# class Grandparents:
#     def show_grandparents(self):
#         print("Grand parents!")
    
# class Parents(Grandparents):
#     def show_parents(self):
#         print("Parents!")

# class Child(Parents):
#     def show_child(self):
#         print("Child!")


# chid = Child()

# chid.show_grandparents()
# chid.show_parents()
# chid.show_child()

# Hierarcheil INHERITANCE:

# one and the childs recive the properties of the  parent.

# class parent:
#     def show(self):
#         print("parent class!")
#     def squaring(self):
#         lists = []
#         for i in range(1,6):
#             lists.append(i ** 2)
#         print(lists)

# class child1(parent):
#     def display1(self):
#         print("child1 class!")

# class child2(child1 , parent):
#     def display2(self):
#         print("child2 class1 ")

# childa = child1()
# childb = child2()
# childc = parent()

# childb.show()
# childa.show()
# childa.squaring()
# childb.display1()
# childb.display2()
# childc.squaring()
# childc.show()