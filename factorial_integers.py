# Factorial n!
# This program can test if the input is 
# a positive integer and calculate its factorial

while True:
    choice = input("START(s) <=> CLOSE (c) ").lower()
    
    if choice == "s":
        num_int = input("Factorial of: ")

        if num_int.isdigit() is True:

            num_int = int(num_int)

            if num_int == 0:
                factorial = 1

            factorial = 1

            for n in range(1,num_int+1):
                factorial *= n 

            print(num_int,"! = ",factorial)

        elif num_int.isdigit() is False:

            print("Can't calculate that dude ...")
            print("Try only positive integers")
            
    elif choice == "c":
        break
        
    else:
        continue
        
