secret_number = 0
guess_number = None
while secret_number != guess_number:
    num=int(input("enter your guess_number :"))
    if secret_number == guess_number:
        print("Congrats,you got the result!")
        break
    else:
        print("Wrong Guess")


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exist")
    choice = int(input("enter choice :"))

    if choice == 1:
        n1 = int(input("enter num1: "))
        n2 = int(input('enter num2: '))
        print("Addition",n1+n2)
    elif choice == 2:
        n1 = int(input("enter num1: "))
        n2 = int(input('enter num2: '))
        print("Addition", n1 - n2)
    elif choice == 3:
        n1 = int(input("enter num1: "))
        n2 = int(input('enter num2: '))
        print("Addition", n1*n2)
    elif choice == 4:
        print("Exist,Thank You")
        break

    else:
        print("invalid choice")



import time
def a(start_time):
    while start_time > 0:
        print(start_time)
        time.sleep(1)
        start_time -= 1
    print("times-up")

start_time = int(input("enter your time :"))
a(start_time)


