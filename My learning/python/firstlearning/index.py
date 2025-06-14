# number = int(input("enter a positive integer "))
# valid_num = False
# while number !=0:
#     print(number-1)
#     number -=1

# num = int(input("enter an integer "))
# multi =1
# while multi < 11:
#     print(num * multi)
#     multi +=1

# print number checker 


# i = 1

# while True:
#     if i <= 5:
#         print(i)
#         i +=1
#         if i > 5:
#             break


# num1 = int(input("enter num :"))
# num2 = int(input("enter num :"))

# while True:
#     avg = (num1 + num2) / 2
#     print(f"The average is {avg}")
#     break

# total_item_purchased = int(input("enter total item purchased"))

# total_price = 0

# for i in range(total_item_purchased):
#     item_price = float(input("enter the item price "))
#     total_price += item_price
#     i +=1

# if total_price >100:
#     discount = 0.1 * total_price
# elif total_price > 50 or total_price < 100:
#     discount = 0.5 * total_price
# else:
#     discount = 0
# total_bill = total_price - discount
# print("subtotal",total_bill)

# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(f"Sum = {total}")

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1,n + 1):
#     factorial = factorial * i

# print(f"factorial = ",factorial)
# n = int(input("enter a number "))

# for i in range(0,n+1):
#     table = n * i
#     print(f"{n} x {i} = {table}")

# number = [1,2,3,4,5]

# even = 0
# odd = 0
# for i in number:
#     if i % 2==0:
#         even +=1
#     else:
#         odd +=1
# print(f"even : {even} , odd : {odd}")

# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# common = []
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print(common)  # Output: [2, 3]


# text = "hello"
# frequency = {}
# for char in text:
#     frequency[char] = frequency.get(char, 0) + 1
# print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# numbers = [-1, 2, 3, -4, 5]
# positive = [num for num in numbers if num > 0]
# average = sum(positive) / len(positive) if positive else 0
# print(round(average, 2))  # Output: 3.33

n = 3
# # Upper half
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# # Lower half
# for i in range(n-2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# def exam_score(score):
#     print("The maximum score is ",max(score))
#     print("The manimum score is ", min(score))
#     print("The average score is", sum(score)/len(score))  # Calculate average manually
#     fail = []
#     passed = []
#     for i in score:
#         if i >= 80:
#             passed.append(i)
#         else:
#             fail.append(i)
#     print("the number of passed student is ", len(passed))
#     print("the number of failed student is ", len(fail))
#     print("passed ",passed)
#     print("failed" ,fail)
# score = [85,92,78,90,88,95,82,79,87,91]
# exam_score(score)
# def exam_score(score):
#     print("Maximum  ",max(score))
#     print("Manimum  ", min(score))
#     print("Average ", sum(score)/len(score))  # Calculate average manually
#     fail = 0
#     passed = 0
#     for i in score:
#         if i >= 80:
#             passed +=1
#         else:
#             fail +=1
#     print("passed ",passed)
#     print("failed" ,fail)
# score = [85,92,78,90,88,95,82,79,87,91]
# exam_score(score)

# def grade_distrubution(marks):
#     for num in marks:
#         if num > 90 and num <= 100:
#             print("Grade: A")
#         elif num >= 80:
#             print("Grade: B")
#         elif num >= 70:
#             print("Grade: C")
#         elif num >= 60:
#             print("Grade: D")
#         elif num >= 50:
#             print("Grade: F")
#         else:
#             print("sorry fail")
        
#     return

# marks = sorted([95,86,78,69,55,33,45,65,98])
# grade_distrubution(marks)

# import random

# def geuss_num():
#     random_num = random.randint(0,100)
#     print(random_num)
#     print("Welcome to number guessing Game ")
#     print("I have choosen a number between 1 and 100. Can you guess it ?")
#     guess = 0
#     attemps = 0
#     while guess != random_num:
#         guess = int(input("Guess number: "))
#         attemps +=1
#         if guess > random_num:
#             print("Too high. Try again")
#         elif guess < random_num:
#             print("Too low. Try again")
#         else:
#             print("Congratuation you guess the correct number")
#             print("The number of attempting the guessing number is ", attemps)
        
# geuss_num()

# def sum_squring(n):
#     total = 0
#     for i in range(1, n+1):
#         total +=i**2 
#     print(f"The sum of square of the first natural number: {total}")   
#     return
# sum_squring(n=int(input("enter a num: ")))
# count = 0
# while count < 5:
#     print("Hello word!")
#     count +=1
