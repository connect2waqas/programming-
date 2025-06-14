import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (l), or correct (c)").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay!, The computer guess the right number! ")

computer_guess(10)