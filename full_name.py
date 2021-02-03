def main():
    try:
        print("Unit tests 1:")
        firstName = "jacob123"
        lastName = "balin456"
        print("Your full name is ", firstName, "", lastName, "\n")
    except:
        print("Unit test 1 failed.")

    try:
        print("Unit tests 2:")
        firstName = 5
        lastName = 6
        print("Your full name is ", firstName, "", lastName, "\n")
    except:
        print("Unit test 2 failed.")

    try:
        print("Unit tests 3:")
        firstName = 6
        lastName = "balin"
        print("Your full name is ", firstName, "", lastName, "\n")
    except:
        print("Unit test 3 failed.")

    running = True
    while(running):
        firstName = input("\nEnter your first name: ")
        lastName = input("\nEnter your last name: ")
        print("\nYour full name is ", firstName, "", lastName, "\n")

        running2 = True
        while(running2):
            print("Would you like to enter another name?")
            keepGoing = input("Enter y for yes or n for no: ")

            if(keepGoing == "n"):
                print("\nGoodbye!")
                running2 = False
                running = False
            elif(keepGoing == "y"):
                running2 = False
            else:
                print("\nIncorrect input. Please try again.\n")



if __name__ == "__main__":
    main()