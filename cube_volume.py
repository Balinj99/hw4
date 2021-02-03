def main():
    print("Unit test 1:")
    length = -5
    if(length < 0):
        length = -length
    print("The volume of a cube of length", length, "is ", length ** 3)

    print("Unit test 1:")
    length = -5.0
    if(length < 0):
        length = -length
    print("The volume of a cube of length", length, "is ", length ** 3)

    print("Unit test 1:")
    length = 5.0
    if(length < 0):
        length = -length
    print("The volume of a cube of length", length, "is ", length ** 3)


    running = True
    while(running):
        try:
            length = float(input("\nPlease enter length: "))
            if(length < 0):
                length = -length

        except:
            print("\nIncorrect input, please try again.")
            continue

        else:
            print("\nThe volume of a cube of length", length, "is ", length ** 3)
        
        running2 = True
        while(running2):
            print("\nWould you like to calculate another volume?")
            keepGoing = input("Enter y for yes or n for no: ")

            if(keepGoing == "n"):
                print("\nGoodbye!")
                running2 = False
                running = False
            
            elif(keepGoing == "y"):
                running2 = False
            
            else:
                print("\nIncorrect input. Please try again.")
            

if __name__ == "__main__":
    main()