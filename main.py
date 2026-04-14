
import random
n=random.randint(1,100)
a=-1
guesses=1
while (a!=n):
    a=int(input("Guess the no. :"))
    if (a>n):
        print("Lower No. Please :")
        guesses+=1
    elif (a<n):
        print("Higher No. Please")
        guesses+=1
print(f"You have guessed no. {n} correctly in {guesses} Attempts")

