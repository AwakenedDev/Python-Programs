def main():
    """
    In this method we prompt user for commands that does a specific task
    """
    list = []
    print ("\n* * *Floating-point program started * * *")
    response = input("\nEnter a command: ").split() #prompt the user to input a command
    x = response[0]
    while x != "End": #while the user doesnt type "End", this program will keep prompting the user for a command
        if x == "Insert": #condition check for "Insert"
            y = response[1]
            try: #check if insert command has a parameter
                y = float(y)
                list.insert(0, y)
                print("\nThe array currently contains:")
                for i in range(len(list)):
                    print("Values[" + str(i) + "]: " + str(format(list[i], '.5f')))
            except ValueError:
                print("\nError: Incorrect floating point value entered")
        elif x == "Delete":#condition check for "Delete"
            y = response[1]
            try:
                y = float(y)
                try:
                    list.remove(y)
                    print("\nThe array currently contains:")
                    for i in range(len(list)):
                        print("Values[" + str(i) + "]: " + str(format(list[i], '.5f')))
                except ValueError:
                    print("Error: Value to be deleted was not found")
                    pass
            except ValueError:
                print("\nError: Incorrect floating point value entered")
        elif x == "Sum": #condition check for "Sum"
            a = sum(list)
            print("The total is " + str(a))
        else:
            print("\nError: Invalid command entered (Try: Insert <number>, Delete <number>, Sum or End to quit") #prints an error if user enters an invalid command

        response = input("\nEnter a command: ").split() #program will keep prompting the user for a command
        x = response[0]

if __name__ == "__main__":
    main()
