import time
def fib(n):
    """
    This method reads a postive integer and then prints the nth Fibonacci number.
    :param n:
    :return value of the nth fibonacci number:
    """
    if n > 1:
        return fib(n-1)+fib(n-2)
    return n

def main():
    """
    This method reads a postive integer and then prints the nth Fibonacci number.
    """
    print("\n* * * Fibonacci Printer * * *\n")
    number = input("Which Fibonacci number would you like to see: ") #here we ask for the user input
    if not number:
        print("Error: No input available")
    else:
        number = int(number)
        if (number > 0) & (number < 46):#condition check for positive numbers
            ti = time.time() #calculate the start time
            fibNum = fib(number)
            tf = time.time() #calculate the end time
            print("\nFibonacci number %d is: %d\n" % (number, fibNum))
            print("This calculation required %f seconds" % (tf-ti)) #print the total time
        else:
            print("Error: Input is out of range")

if __name__ == "__main__":
    main()


