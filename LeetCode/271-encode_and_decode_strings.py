"""

https://leetcode.com/problems/encode-and-decode-strings/ (Premium Access Only)

https://neetcode.io/problems/string-encode-and-decode (Free NeetCode Link)

Design an algorithm to encode a list of strings to a single string. The encoded
string is then decoded back to the original list of strings.

Please implement encode and decode functions.

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

def encode(strs: list[str]) -> str:
    result = ''
    for word in strs:
        result += str(len(word)) + '#' + word
    return result

def decode(s: str) -> list[str]:
    result = []
    i = 0
    
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        
        length = int(s[i:j])
        result.append(s[(j+1):(j+1+length)])
        i = j + 1 + length
    return result

if __name__ == '__main__':
    strs = ["neet", "code", "love", "you"]
    print("Input String   :", strs)
    encodedString = encode(strs)
    print("Encoded String :", encodedString)
    decodedString = decode(encodedString)
    print("Decoded String :", decodedString)
    assert(decodedString == strs)