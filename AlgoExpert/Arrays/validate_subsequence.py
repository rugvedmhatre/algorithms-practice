# Validate Subsequence
# Array = [0, 1, 2, 3, 4, 5, 6, 9, -1, 8, 10]
# Subsequence = [1, 6, -1, 10]
# O(N) time, O(1) space

def validate_subsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)

# -- Another Method --
# def validate_subsequence(array, sequence):
#     sequenceIdx = 0
#     for value in array:
#         if sequenceIdx == len(sequence):
#             break
#         if value == sequence[sequenceIdx]:
#             sequenceIdx += 1
#     return sequenceIdx == len(sequence)

if __name__ == '__main__':
    array_a = [0, 1, 2, 3, 4, 5, 6, 9, -1, 8, 10]
    subsequence = [1, 6, -1, 10]
    print(validate_subsequence(array_a, subsequence))