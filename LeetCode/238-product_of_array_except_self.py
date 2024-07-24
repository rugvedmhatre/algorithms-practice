

def productExceptSelf(nums: list[int]) -> list[int]:
    zeros_count = nums.count(0)
    result = []

    if zeros_count < 1:
        total_product = 1
        for number in nums:
            total_product = total_product * number
        for number in nums:
            result.append(total_product // number)
    elif zeros_count == 1:
        total_product = 1
        for number in nums:
            if number != 0:
                total_product = total_product * number
        for number in nums:
            if number == 0:
                result.append(total_product)
            else:
                result.append(0)
    else:
        for number in nums:
            result.append(0)

    return result

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelf(nums))