def max_pairwise_product(numbers):
    first_maxnumber_index = numbers.index(max(numbers))
    first_maxnumber = numbers.pop(first_maxnumber_index)
    second_maxnumber_index = numbers.index(max(numbers))
    second_maxnumber = numbers.pop(second_maxnumber_index)
    return first_maxnumber * second_maxnumber

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))