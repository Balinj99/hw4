def main():
    try:
        print("Unit test 1:")
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("nAverage: ", ave, "\n")
    except:
        print("Unit test 1 failed.\n")

    try:
        print("Unit test 2:")
        arr = [-1, -2, -3, -4, -5]
        total = 0
        for i in arr:
            total += i
    
        ave = total / len(arr)
        print("Average: ", ave, "\n")
    except:
        print("Unit test 2 failed.\n")

    try:
        print("Unit test 3:")
        arr = [1, -2, 3, -4, 5]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("Average: ", ave, "\n")
    except:
        print("Unit test 3 failed.\n")

    try:
        print("Unit test 4:")
        arr = []
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("Average: ", ave, "\n")
    except:
        print("Unit test 4 failed.\n")

    try:
        print("Unit test 5:")
        arr = [1.0, 2.1, 3.2, 4.3, 5.4]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("Average: ", ave, "\n")
    except:
        print("Unit test 5 failed.\n")

    try:
        print("Unit test 6:")
        arr = [1, 2.1, 3, 4.3, 5]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("Average: ", ave, "\n")
    except:
        print("Unit test 6 failed.\n")

    running = True
    while(running):
        try:
            num = int(input("Enter the number of elements in your list: "))

        except:
            print("\nIncorrect input. Please try again.")
            continue

        else:

            for n in range(0,num):

                running2 = True

                while(running2):

                    try:
                        arr[n] = float(input("Enter the value of this element: "))

                    except:
                        print("\nIncorrect input. Please try again.")
                        continue
                    
                    else:
                        running2 = False

            total = 0

            for i in arr:
                total += i

            ave = total / len(arr)
            print("\nAverage: ", ave, "\n")    

        running3 = True
        while(running3):
            print("Would you like to repeat the process?")
            keepGoing = input("\nEnter y for yes or n for no: ")

            if(keepGoing == "n"):
                print("\nGoodbye!")
                running3 = False
                running = False
            elif(keepGoing == "y"):
                print()
                running3 = False
            else:
                print("\nIncorrect input. Please try again.")


if __name__ == "__main__":
    main()