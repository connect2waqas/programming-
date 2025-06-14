# # CREATING SIMPLE DICTIONARY
# personal = {
#     "name" : "swati",
#     "age"  :  30,
#     "city" : "Banglour"
# }

# print(personal,"\n",type(personal))

# dictionary can store any type of data

# mixed_dict = {
#     "name" : "waqas",
#     "age" : 20,
#     "is_student" : True,
#     "courses" : ["physics","biology","chemistry"],
#     "address" :{
#         "street" : "Timergara talash 123",
#         "city" : "Timergara",
#         "postal_code" : 18300
#     }
# }

# print(mixed_dict, "\n", type(mixed_dict))
# 1 method: By construtor method:

# empty_dict = dict(name = "swati",age = 23, roll_no = 2004, is_student = True , city = "timeragara")
# print(empty_dict,"\n",type(empty_dict))

# empty_dict1 = {}
# print(empty_dict1,"\n",type(empty_dict1))

#  DICTIONARY COMPREHENSION:
# it is performation operation that is more faster that loops in python

# square = {x: x*x for x in range(5)}

# print(square)

# product_details = {}

# products = int(input("Enter the total number of Products:"))

# for product in range(products):
#     product_ID = int(input(f"Enter the Product ID for Product {product+1}"))
#     product_name = input(f"Enter the Product Name for Product {product+1}")

#     product_details.update({product_ID : product_name})

# print("The final dictionary containing all product IDs and names :")
# print(product_details)
# print(type(product_details))

# products_details = {}

# products = int(input("enter the number of products: "))

# for product in range(products):
#     product_ID = int(input(f"enter the product id for product {product+1}: "))
#     product_name = input(f"enter the product name for product {product+1}: ")

#     products_details.update({product_ID : product_name})

# print("the final dictionary containing all products IDs and names: ")
# print(products_details)
# print(type(products_details))

# person = {
#     "name" : "waqas",
#     "age"  : 20,
#     "is_student" : True
# }

# print(person["name"],"\n",person["is_student"],"\n",person["age"])

# ordering of dictionary :
# dictionary was not have any specific order before 3.7 and after 3.7 
# the order was maintain okay we get the result as we have write:

# my_dict ={
#     "name":"waqas",
#     972 : "integer",
#     3.7 : "python",
#     (1,2,3) : "tuple",
#     "rollno" : "integer"
# }

# print(my_dict)

# we cannot used the duplicate in dictionary :

