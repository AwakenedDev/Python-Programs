class Commands:
    """
    This class contains the to do list (myList) and provides methods that modify the list as required
    """

    #declaration of variable
    global myList
    myList = []
    myString = ""
    number1 = 0
    number2 = 0
    number = 0

    def show(self):
        """
        this method displays the values in the list
        :return:my list
        """
        return myList
    def add(self, myString):
        """
        in this method we add an item(i.e string, number e.t.c) to the end of the list)
        :param myString:
        """
        self.myString = myString
        myList.append(myString)
    def move(self, number1 , number2):
        """

        :param number1:
        :param number2:
        """
        self.number1 = number1
        self.number2 = number2
        if (0 < self.number1 <= len(myList)) & (0 < self.number2 <= len(myList)):#added optional error checking
            string = myList[self.number1-1]
            del myList[self.number1-1]
            myList.insert((self.number2-1), string) #moves item number1 in the list to position number2
        else:
            print("Error: Move Unsuccessful")
    def complete(self, number):
        """
        in this method we mark a specified item in the list
        :param number:
        """
        self.number = number
        if (0 < number <= (len(myList))):
            del myList[number-1] #basically the items gets deleted from the list
        else:
            print("Error: %i is not available" % number)

class InputOutput:
    """
    In this class, we prompt the user for a command and then read the response and call the Commands' class
    """
    def main():
        print("\n* * * To Do List * * *")
        response = input("\nEnter a command(Show, Add, Move, Complete) or End:\n") #ask for user response
        respList = response.split()
        a = respList[0]

        myToDoList = Commands()

        while a != "End": #program keeps prompting user to input commands untill user types "End"
            try: #condition check
                if a == "Show":
                    listCopy = myToDoList.show()
                    for i in range(len(listCopy)):
                        print(str(i+1) + ". " + str(listCopy[i]))
                elif a == "Add":
                    string = response.split(' ', 1)
                    string2 = string[1] #breaks the the resonse into two parts
                    if not string2: #additional error checking
                        print("Error: Wrong or No input")
                    else:
                        myToDoList.add(string2)
                elif a == "Move":
                    string = response.split(' ', 2)
                    if string[1].isdigit() & string[2].isdigit():  #additional error checking
                        num2 = int(string[1])#break the response into 3 parts
                        num3 = int(string[2])
                        myToDoList.move(num2, num3)
                    else:
                        print("Error: Wrong or No input")
                elif a == "Complete":
                    num = response.split(' ', 1) #breaks the response into two parts
                    if num[1].isdigit(): #additional error checking
                        num2 = int(num[1])
                        myToDoList.complete(num2)
                    else:
                        print("Error: Wrong or No input")
                else:
                    print(str(a) + " is an unrecognized command")
            except IndexError:
                print("Error: Wrong or No input")

            response = input("\nEnter a command(Show, Add, Move, Complete) or End:\n") #keep reprompting the user to enter command until "End" is entered
            respList = response.split()
            a = respList[0]
    if __name__ == "__main__":
        main()