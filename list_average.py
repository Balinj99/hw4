def main():
    arr = [1, 2, 3, 4, 5]
    total = 0
    for i in arr:
        total += i

    ave = total / len(arr)
    print("\nAverage: ", ave, "\n")
        
if __name__ == "__main__":
    main()