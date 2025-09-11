"""

https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits signed integer.


Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 

Constraints:
- 0 <= n <= 2^31 - 2
- n is even.


Follow up: If this function is called many times, how would you optimize it?

"""

def reverseBits(n: int) -> int:
    result = 0

    for i in range(32):
        bit = (n >> i) & 1
        result = result | (bit << (31 - i))
    
    return result

if __name__ == "__main__":
    # Test Case 1
    n = 43261596
    print(reverseBits(n))

    # Test Case 2
    n = 2147483644
    print(reverseBits(n))