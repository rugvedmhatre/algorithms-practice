"""

https://leetcode.com/problems/encode-and-decode-strings/ (Premium Access Only)

https://www.lintcode.com/problem/659/ (Free Lintcode Link)

Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of 
strings.

Please implement encode and decode functions.

Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

"""

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    result = ''
    for word in strs:
        result += str(len(word)) + '#' + word
    return result

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    result = []
    i = 0
    
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        
        length = int(str[i:j])
        result.append(str[(j+1):(j+1+length)])
        i = j + 1 + length
    return result

if __name__ == '__main__':
    strs = ["lint", "code", "love", "you"]
    print("Input String   :", strs)
    encodedString = encode(strs)
    print("Encoded String :", encodedString)
    decodedString = decode(encodedString)
    print("Decoded String :", decodedString)
    assert(decodedString == strs)