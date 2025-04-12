"""

https://leetcode.com/problems/find-the-count-of-good-integers/

You are given two positive integers n and k.

An integer x is called k-palindromic if:
- x is a palindrome.
- x is divisible by k.

An integer is called good if its digits can be rearranged to form a k-palindromic integer. For 
example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010
cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For 
example, 1010 cannot be rearranged to form 101.
 

Example 1:
Input: n = 3, k = 5
Output: 27
Explanation:
Some of the good integers are:
551 because it can be rearranged to form 515.
525 because it is already k-palindromic.

Example 2:
Input: n = 1, k = 4
Output: 2
Explanation:
The two good integers are 4 and 8.

Example 3:
Input: n = 5, k = 6
Output: 2468
 

Constraints:
- 1 <= n <= 10
- 1 <= k <= 9

"""

from collections import Counter
from math import factorial
from itertools import product

def countGoodIntegers(num_digits: int, divisor: int) -> int:
    valid_digit_frequencies = set()

    def frequency_to_tuple(freq_dict):
        return tuple(freq_dict.get(str(digit), 0) for digit in range(10))

    def construct_palindrome(left_half, middle_digit=""):
        return "".join(left_half) + middle_digit + "".join(reversed(left_half))

    if num_digits == 1:
        for single_digit in range(1, 10):
            if single_digit % divisor == 0:
                valid_digit_frequencies.add(frequency_to_tuple(Counter(str(single_digit))))
    else:
        half_length = num_digits // 2
        all_digits = '0123456789'

        left_half_combinations = product(all_digits, repeat=half_length)

        if num_digits % 2 == 0:
            for left_half in left_half_combinations:
                if left_half[0] == '0':
                    continue  
                palindrome_str = construct_palindrome(left_half)
                palindrome_value = int(palindrome_str)
                if palindrome_value % divisor == 0:
                    valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))
        else:

            for left_half in left_half_combinations:
                if left_half[0] == '0':
                    continue 
                for middle_digit in all_digits:
                    palindrome_str = construct_palindrome(left_half, middle_digit)
                    palindrome_value = int(palindrome_str)
                    if palindrome_value % divisor == 0:
                        valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))


    total_valid_permutations = 0
    for freq_tuple in valid_digit_frequencies:
        digit_counts = list(freq_tuple)


        total_permutations = factorial(num_digits)
        for count in digit_counts:
            total_permutations //= factorial(count)

        invalid_permutations = 0
        if digit_counts[0] > 0:
            remaining_counts = digit_counts.copy()
            remaining_counts[0] -= 1
            invalid_permutations = factorial(num_digits - 1)
            for count in remaining_counts:
                invalid_permutations //= factorial(count)

        valid_permutations = total_permutations - invalid_permutations
        total_valid_permutations += valid_permutations

    return total_valid_permutations

if __name__ == "__main__":
    # Test Case 1
    n = 3
    k = 5
    print(countGoodIntegers(n, k))

    # Test Case 2
    n = 1
    k = 4
    print(countGoodIntegers(n, k))

    # Test Case 3
    n = 5
    k = 6
    print(countGoodIntegers(n, k))