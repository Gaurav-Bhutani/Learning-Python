import random

def fun():
    play = True
    while play:
        n = random.randint(1,100000)
        num=int(input("Enter the number: "))
        diff=num-n
        if diff==0:
            print("You Entered the correct choice")
        while diff != 0:
            if(num>=n):
                print("Entered number is too high")
                diff = False
            else:
                print("Entered number is too low")
                diff = False
        temp=input("Press ENTER to try again  or  Press 0 to exit:\t")
        if(temp=='0'):
            play = False

player=input('Please enter your name: ')
print("\nHello " + player + "...!!\n")
print("This program will randomely generate a number you have to guess it.")

fun()
