# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right) // 2
    a_left = get_majority_element(a, left, mid)
    a_right = get_majority_element(a, mid, right)

    count1, count2 = 0, 0
    for i in a[left:right]:
        if i == a_left:
            count1 += 1
        elif i == a_right:
            count2 += 1
    if count1 > ((right - left) // 2) and a_left != -1:
        return a_left
    elif count2 > ((right - left) // 2) and a_right != -1:
        return a_right
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
