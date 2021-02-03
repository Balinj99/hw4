def main():
    try:
        print("Unit test 1:")
        arr = [1, 2, 3, 4, 5]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("\nAverage: ", ave, "\n")
    except:
        print("Unit test 1 failed.")

    try:
        print("Unit test 2:")
        arr = [-1, -2, -3, -4, -5]
        total = 0
        for i in arr:
            total += i
    
        ave = total / len(arr)
        print("\nAverage: ", ave, "\n")
    except:
        print("Unit test 1 failed.")

    try:
        print("Unit test 3:")
        arr = [1, -2, 3, -4, 5]
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("\nAverage: ", ave, "\n")
    except:
        print("Unit test 3 failed.")

    try:
        print("Unit test 4:")
        arr = []
        total = 0
        for i in arr:
            total += i

        ave = total / len(arr)
        print("\nAverage: ", ave, "\n")
    except:
        print("Unit test 4 failed.")

        
if __name__ == "__main__":
    main()