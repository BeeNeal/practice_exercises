import random


print "Hello!"

name = raw_input("Hey, what's your name? \n")

rand_num = random.randint(1, 101)
print rand_num
count = 0
while True:
    guess = raw_input("Guess a number!")
    count += 1
    if int(guess) > rand_num:
        print "That's too high"
    elif int(guess) < rand_num:
        print "that's too low"
    elif int(guess) == rand_num:
        print "You got it in {} tries!" .format(count)
        break
