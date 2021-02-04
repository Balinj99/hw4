def ave(arr):
    total = 0
    if(arr == []):
        return 0
    else:
        for i in arr:
            total += i
        return total / len(arr)