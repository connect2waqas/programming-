# write a python code to concatenate the following dictionaries into a new one okay

# name = {
#     "emp1" : "waqas",
#     "emp2" : "ilyas",
#     "emp3" : "abbas"
# }
# age = {
#     "age1" : 20,
#     "age2" : 17 ,
#     "age3" : 12
# }

# occupaction = {
#     "waqas" : "AI engineer",
#     "ilyas" : "Electronic engineer",
#     "abbas" : "Student"
# }

# concatenation = {}
# for i in (name,age,occupaction):concatenation.update(i) # this also works in python
    
# print(concatenation)

#  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# square = {}
# def squars_dict(square):
#     for i in range(1,11):
#         square[i] = i**2
#     print(square)
# squars_dict(square)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # slowly working approach is this:
# profile = {
#     "name" : "waqas",
#     "age" : 20,
#     "status" : "AI engineer",
#     "hobby" : "learning technology"
# }

# def key_check(profile):
#     for i in profile:
#         if i == "name":
#             print("Yes already exist!")
    
# key_check(profile)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # but the best approach is the following one:

profile = {
    "name" : "waqas",
    "age" : 20,
    "status" : "AI engineer",
    "hobby" : "learning technology"
}

def check_keys(x):
    if x in profile:
        print("Yes already exist!")
    else:
        print("No Does not exist!")


check_keys(x=input("Enter a key: "))