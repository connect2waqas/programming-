# OBJECT ORIENTED PROGRAMMING:
# IN today lecture will discuss the following topic of OOPs:
# 1) Procedural programming
# 2) Functional programming
# 3) object oriented programming
# 4) Difference between programming paradigm
# 5) Class
# 6) Object
# 7) self
# 8) init function
# 9) practice questions

# procedural programming

# addition through procedural programming
# num1 = 10
# num2 = 20

# sum = num1 + num2

# print(sum)

# ////////////////functional programming///////////////////////////

# def sum(a ,b):
#     add = a + b
#     print(add)
# sum(10,20)

# //////////////object oriented programming/////////////////////
# DOING THE ABOVE THROUGH OBJECT ORIENTED PROGRAMMING ////////

# creating a class:
# class calculator:
#     def sum(self, a, b):
#         print(a + b)
#     def diff(self, a , b):
#         print(a - b)
#     def multi(self, a , b):
#         print(a * b)
#     def division(self , a , b ):
#         print(a // b)

# # creating a object for a class:
# cal = calculator()
# cal.sum(30,20)
# cal.multi(40,2)
# cal.division(90,3)
# /////////// our example for this//////////////

# class Car:
#     def start(self):
#         print(f"The {self.colur} {self.model} car is starting.")
    



# car1 = Car()
# car1.model = "Toyta"
# car1.colur = "Blue"

# car2 = Car()
# car2.model = "Honda"
# car2.colur = "Red"

# car1.start()
# car2.start()

# /// init functions ////

class Car:
    def __init__(self,colur,model,speed):
        self.colur = colur
        self.model = model
        self.speed = speed
    def start(self):
        print(f"The {self.colur} {self.model} with {self.speed} is starting..")
    
car1 = Car("Black" , "Toyota" ,200)

car1.start()
        

