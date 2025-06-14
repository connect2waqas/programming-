# class Car():
#     def start(self):
#         print("CAR IS STARTING....")
#     def stop(self):
#         print("CAR IS STOPING....")

# car1 = Car()
# car2 = Car()

# car1.start()
# car1.stop()


# class Student:
#     def __init__(self):
#         print("Adding new student to the data base..")


# s1 = Student()

# print(s1)


# class Database:
#     colloge_name = "Apna college"
#     def __init__(self,name,roll_no,age,):
#         print("Adding students to the database")
#         self.name = name # left side name should be same the parameter okay..
#         self.roll_no = roll_no # all of this is instance attributes
#         self.age = age

# s1 = Database("Ilyas","0440",18)
# print(f"The {s1.name} has roll no : {s1.roll_no} with the age: {s1.age} of the {Database.colloge_name}")
# s2 = Database("Abbas","0457",12)
# print(f"The {s2.name} has roll no : {s2.roll_no} with the age: {s2.age} of the {Database.colloge_name}")


# class Student:
#     def __init__(self,name , marks):
#         self.name = name 
#         self.marks = marks
#     def avg(self):
#         sum = 0
#         for i in self.marks:
#             sum +=i
#         print(f"Hi {self.name} you avg score marks is:  {sum/3} ")

# s1 = Student("waqas",marks=[43,52,30])
# s1.avg()
conda create --name myoop