import random
lower_bound=int(input("Set the lower limit : "))
upper_bound=int(input("Set the upper limit : "))
max_attempts=5
target_number = random.randint(lower_bound, upper_bound)
for attempt in range(max_attempts):
    guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break
if(attempt == max_attempts-1):
    print("The attempts are over")