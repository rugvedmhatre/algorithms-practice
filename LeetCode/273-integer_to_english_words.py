"""

Convert a non-negative integer num to its English words 
representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand 
Five Hundred Sixty Seven"
 

Constraints:
0 <= num <= 2^31 - 1

"""

def solution(num: int) -> str:
    if num == 0:
        return "Zero"
    
    bigString = ["Thousand", "Million", "Billion"]
    result = numberToWordsHelper(num % 1000)
    num //= 1000
    
    for i in range(len(bigString)):
        if num > 0 and num % 1000 > 0:
            result = numberToWordsHelper(num % 1000) + bigString[i] + " " + result
        num //= 1000
    
    return result.strip()

def numberToWordsHelper(num: int) -> str:
    digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    result = ""
    if num > 99:
        result += digitString[num // 100] + " Hundred "
    
    num %= 100
    if num < 20 and num > 9:
        result += teenString[num - 10] + " "
    else:
        if num >= 20:
            result += tenString[num // 10] + " "
        num %= 10
        if num > 0:
            result += digitString[num] + " "
    
    return result

def numberToWords(num: int) -> str:
    result = ''
    
    if num == 0:
        return "Zero"
    
    if num >= 1_000_000_000:
        result += helper(num // 1_000_000_000) + ' Billion '
        num = num % 1_000_000_000

    if num >= 1_000_000:
        result += helper(num // 1_000_000) + ' Million '
        num = num % 1_000_000

    if num >= 1_000:
        result += helper(num // 1_000) + ' Thousand '
        num = num % 1000
    
    result += helper(num)
    
    return result.strip()
    

def helper(num):
    result = ''

    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    hundredsIdx = num // 100
    if num >= 100 and hundredsIdx < 10:
        result += ones[hundredsIdx] + ' Hundred '
    num = num % 100

    teensIdx = num % 100
    if 9 < teensIdx < 20:
        result += teens[teensIdx % 10]
        return result.strip()
    elif teensIdx >= 20:
        result += tens[(teensIdx // 10) - 2] + ' '

    onesIdx = num % 10
    result += ones[onesIdx]

    return result.strip()

def test_case_1():
    num = 0
    answer = numberToWords(num)
    print(str(num) + ' : ' + answer)
    assert(answer == "Zero")

def test_case_2():
    num = 123
    answer = numberToWords(num)
    print(str(num) + ' : ' + answer)
    assert(answer == "One Hundred Twenty Three")

def test_case_3():
    for i in range(1, 11):
        num = i
        answer = numberToWords(num)
        print(str(num) + ' : ' + answer)

def test_case_4():
    for i in range(0, 1_000_000):
        num = i
        answer = numberToWords(num)
        # print(str(num) + ' : ' + answer)
        assert(answer == solution(num))

def test_case_5():
    num = 1_345_234_567
    answer = numberToWords(num)
    print(str(num) + ' : ' + answer)
    assert(answer == solution(num))

if __name__ == '__main__':
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    test_case_5()