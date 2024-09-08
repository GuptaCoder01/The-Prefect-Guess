import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess the number :"))
    if(a > n):
        print("Too high!")
    else:
        print("Too low!")
print(f"you have guessed th enumber {n} correctly in {guesses} attempts")