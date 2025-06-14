import random

def guess(x):
    random_num = random.randint(1,x)
    print(random_num)
    guess = 0
    while guess != random_num:
        guess = int(input("guess a number: "))
        print(guess)
        if guess < random_num:
            print("Sorry! : Too low enter again1")
        elif guess > random_num:
            print("Sorry! Too high enter again!")
    print("Yay, Congrats. You have enter a correct number..")

guess(10)