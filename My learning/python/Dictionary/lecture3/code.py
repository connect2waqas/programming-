# METHOD IN DICTIONARY

# profile = {
#     "name " : "waqas khan",
#     "age" : 20,
#     'city' : "timergara",
#     'phone' : 33333333,
    
# }
# # we disscused all the dict method in one function
# def dict_methods(profile):
#     print(len(profile))
#     print(profile.keys())
#     print(profile.values())
#     print(profile.items())
    
# dict_methods(profile)

# changing values in dictionary 

# a = {
#     "name" : "waqas",
#     "age" : 21,
#     'country' :"india"
# }

# print(a) # india
# a["country"] = "pakistan"

# print(a) # pakistan

# a["age"] = 20

# print(a)

# Adding items to a dictionary

# 1) simple method 

# person = {
#     "name" : "alas",
#     "age" : 30
# }

# print(person)

# person["city"] = "united kingdom"
# person["email_id"] = "ali@gmail.com"

# print(person)

# 2) BY UPDATE METHOD:


# person = {
#     "name" : "alas",
#     "age" : 30,
#     "gender" : "male",
#     "country" : "united kingdom"
# }

# # print(person)

# person.update({"is_Student": True , "student_ID": 9722 , "phone_id" : 32298})

# print(person)


# REMOVING THE ITEMS FROM THE DICTIONARY:

# By Pop() Method:

profile = {"name": "waqas" , "age": 29 , "Is_student" : True , "country" : "Pakistan" , "gender" : "Male", "Postal code" : 18300}

# print(profile)

# profile.pop("age")
# print(profile)

# BY DELETE METHOD: 

# del profile["age"], profile["country"]

# print(profile)

# del profile

# print(profile) # rises the error becuase of deleting the dictionary and after that we want to print and get wrong result

# print(profile.clear())

# new_profile = profile.copy()

# print(profile)
# print(new_profile)

# a = profile.popitem() # it remove the last item from the dictionary # output : postal : 18300
# b = profile.popitem() # it remove the last item from the dictionary # output : gender : male
# print(a)
# print(b)
# x = profile.pop("age") # it remove the specific key and returns its value okay
# print(x)