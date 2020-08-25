def collatz(number):
    
    if (number % 2 == 0):  # even
        print(number // 2)
        return number // 2
    
    elif (number % 2 == 1):
        print(3 * number + 1)
        return (3 * number + 1)

try:
    userNum = int(input()) # user input -- converting input()to int since it is a string
    while userNum != 1:
        userNum = collatz(userNum)
except ValueError:
    print('You must enter an integer!')





