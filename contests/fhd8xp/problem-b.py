count = 0
guess = 500
print(guess)

new_max = 1000
new_min = 1

while count < 10:
    control = input()

    if control == "higher":
        new_min = guess + 1
        guess = (new_min + new_max)//2

    if control == "lower":
        new_max = guess - 1
        guess = (new_max + new_min)//2
    if control == "correct":
        break

    print(guess)

    count += 1
