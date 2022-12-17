import random

r = random.randrange(-5, 11)  # includes -5 till 10
r1 = random.randint(-5, 11) # includes -5 till 11
print(r)


print("------------------------------start here-------------------------------------")

top_of_range = input("Type a number: ") # always returns a String even if user types in an int

if top_of_range.isdigit() :
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time!")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

# if you use comma to print a string no need to give spaces -> it will do it auto
# also it will automatically convert it into a string
# same as print("You got it in " + str(guesses) +  "guesses")
print("You got it in" , guesses, "guesses") 
