# # Membership testing

# person = {
#     "name" : "waqas",
#     "age"  : 20,
#     "city" : "timergara"
# }

# print("name" in person)

# print("age" in person)

# print("timergara" in person) # we should key only for membership testing

# profile = {
#     "emp1" : {"name":"waqas", "age": 19, "location": "Haripur"},
#     "emp2" : {"name" : "ilyas", "age": 17 , "location": "Talash"},
#     "emp3" : {"name" : "abbas", "age" : 11 , "location": "Talash"}
# }

# print(profile["emp1"]["location"])
# print(profile["emp3"]["name"],profile["emp2"]["age"],profile["emp1"]["location"])

# print(profile["emp1"])

# book_rating = {
#     "python_programming" : 4.5,
#     "Data science Handbook" : 4.8,
#     "Machine learning Basic" : 4.2
# }

# def checkig(book_rating):
#     list_title = []
#     if "python_programming" in book_rating:
#         print("Found")
#     else:
#         print("Not Found")
#     for i in book_rating:
#         list_title.append(i)
#     print(list_title)

# checkig(book_rating)
# title = list(book_rating.keys()) # the best way to get the keys: the above also work.
# print(title)

# PRACTICE QUESTION NO 2:

# friut_stock = {
#     "apple" : 10,
#     "banana" : 15,
#     "orange" : 8,
#     "grape" : 20
# }

# def friut_Stock_count(friut_stock):
#     for i in friut_stock:
#         print(f"Friut: {i} : Stock {friut_stock[i]}")
# friut_Stock_count(friut_stock)

profile = {
    "name " : "waqas khan",
    "age" : 20,
    'city' : "timergara",
    'phone' : 33333333,
    
}