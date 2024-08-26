"""



"""

def replaceElements(arr: list[int]) -> list[int]:
    # if len(arr) == 1:
    #     arr[-1] = -1
    #     return arr

    currentMax = -1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > currentMax:
            arr[i], currentMax = currentMax, arr[i]
        else:
            arr[i] = currentMax
        
    return arr

if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    # arr = [400]
    print(replaceElements(arr))