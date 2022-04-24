from json.tool import main
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"\nAdvinhe um número de 1 a {x}: "))

        if guess < random_number:
            print("\nTente novamente, muito baixo");
        
        elif guess > x:
            print("\nEsse número excede o limite, Tente novamente");

        elif guess > random_number:
            print("\nTente novamente, muito alto");


    print(f"\nMuito bem, esse é número {random_number} \n")


if __name__ == '__main__':
    y = int(input("\nDefina um numero limite: "))
    guess(y)