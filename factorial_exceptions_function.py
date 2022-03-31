#!/usr/bin/env python
while True:
    try:
        print("Write positive integer n to calculate n! ")
        i = int(input("n = "))
        
        if i < 0:
            raise ValueError
        pass

        factorial(i)
        
    except ValueError:
        print(" ******************************* ")
        print("You should write positive integer")

#calculate factorial
def factorial(n):
    integer = 1

    for j in range(1,n+1):
        integer *= j
    
    print(f"{n}! = {integer}")

