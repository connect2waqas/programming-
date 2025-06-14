# here we have to work on the file input and output okay..

# file = open("example.txt","w")
# file.write("Hello this is sample file.")
# file.close()

# try:
#     with open("example.txt","r") as file:
#         content = file.read()
#         print("file content: ",content)
# except FileNotFoundError:
#     print("Error: The file does not exist!")

# with open("example.txt","w") as file:
#     file.write("The file is been override okay!")
# print("File written successfully!")

# with open("example.txt","a") as file:
#     file.write("\nThis is new line add to existing one")
# print("New content added successfully")

# try:
#     with open('example.txt', 'r') as file:
#          content = file.read()
#          print('File Content:', content)
# except FileNotFoundError:
#     print('Error: The file does not exist!')

# with open('example.txt', 'a') as file:
#     file.write('\nThis is a new line added using append mode.')
#     print('New content appended successfully.')
import json
# data = {
#   "name": "Alice",
#   "age": 30,
#   "is_student": False,
#   "courses": ["Math", "Science"],
#   "address": {
#     "city": "New York",
#     "zipcode": "10001"
#   }
# }

# with open("data.json","w") as file:
#     json.dump(data,file)
# with open("data.json","r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)
