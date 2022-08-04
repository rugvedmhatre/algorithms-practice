import math

def binary_search(keys, query):
    low = 0
    high = num_keys - 1
    while (low <= high):
        mid = math.floor(low + ((high - low) / 2))
        if query == keys[mid]:
            return mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Recursive solution
# def binary_search(keys, low, high, query):
    # if high < low:
    #     return -1
    # mid = math.floor(low + ((high - low) / 2))
    # if query == keys[mid]:
    #     return mid
    # elif query < keys[mid]:
    #     return binary_search(keys, low, mid-1, query)
    # else:
    #     return binary_search(keys, mid+1, high, query)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
