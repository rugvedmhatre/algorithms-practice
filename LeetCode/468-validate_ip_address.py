"""

https://leetcode.com/problems/validate-ip-address/

Given a string queryIP, return "IPv4" if IP is a valid IPv4 
address, "IPv6" if IP is a valid IPv6 address or "Neither" 
if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" 
where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 
addresses while "192.168.01.1", "192.168.1.00", and 
"192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form 
"x1:x2:x3:x4:x5:x6:x7:x8" where:
- 1 <= xi.length <= 4
- xi is a hexadecimal string which may contain digits, 
  lowercase English letter ('a' to 'f') and upper-case 
  English letters ('A' to 'F').
- Leading zeros are allowed in xi.

For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 
and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 
addresses, while "2001:0db8:85a3::8A2E:037j:7334" and 
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6
addresses.

Example 1:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:
queryIP consists only of English letters, digits and the 
characters '.' and ':'.

"""

import re

def validIPAddress(queryIP: str) -> str:
    # check if the address is following the IPv4 pattern
    # if yes, return, else:
    # check if the address is following the IPv6 pattern
    # if yes, return, else:
    # return neither

    if isIPv4(queryIP):
        return "IPv4"
    elif isIPv6(queryIP):
        return "IPv6"
    else:
        return "Neither"
    
def validIPAddressRegEx(queryIP: str) -> str:
    iPv4_chunk = "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    iPv4_pattern = '^(' + iPv4_chunk + '\\.){3}' + iPv4_chunk + '$'

    iPv6_chunk = "([0-9a-fA-F]{1,4})"
    iPv6_pattern = '^(' + iPv6_chunk + ':){7}' + iPv6_chunk + '$'

    if re.fullmatch(iPv4_pattern, queryIP):
        return "IPv4"
    elif re.fullmatch(iPv6_pattern, queryIP):
        return "IPv6"
    else:
        return "Neither"
    
def isIPv4(queryIP: str) -> bool:
    if queryIP.count('.') != 3:
        return False
    
    queryIPlist = queryIP.split('.')

    if len(queryIPlist) != 4:
        return False
    
    for number in queryIPlist:
        if re.search("[a-zA-z]", number) != None:
            return False
        
        if len(number) > 3 or len(number) == 0:
                return False
        
        if int(number) > 255 or int(number) < 0:
            return False
        
        if number.startswith('0') and len(number) != 1:
            return False
    
    return True

def isIPv6(queryIP: str) -> bool:
    if queryIP.count(':') != 7:
        return False
    
    queryIPlist = queryIP.split(':')

    if len(queryIPlist) != 8:
        return False

    for number in queryIPlist:
        if len(number) > 4 or len(number) == 0:
            return False
        
        if re.search("[g-zG-Z]", number) != None:
            return False
    
    return True

if __name__ == "__main__":
    # Test Case 1
    queryIP = "172.16.254.1"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "IPv4"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "IPv4"
    
    # Test Case 2
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "IPv6"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "IPv6"
    
    # Test Case 3
    queryIP = "256.256.256.256"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"

    # Test Case 4
    queryIP = "192.168.1.0"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "IPv4"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "IPv4"

    # Test Case 5
    queryIP = "192.168.01.1"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"

    # Test Case 6
    queryIP = "192.168.1.00"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"

    # Test Case 7
    queryIP = "192.168@1.1"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"

    # Test Case 8
    queryIP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "IPv6"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "IPv6"
    
    # Test Case 9
    queryIP = "2001:0db8:85a3::8A2E:037j:7334"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"

    # Test Case 10
    queryIP = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(validIPAddress(queryIP), ':', queryIP) # Output: "Neither"
    print(validIPAddressRegEx(queryIP), ':', queryIP) # Output: "Neither"