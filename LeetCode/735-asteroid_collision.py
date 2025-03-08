"""

https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row. The indices of the 
asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one 
will explode. If both are the same size, both will explode. Two asteroids moving in the same 
direction will never meet.
 

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

"""

def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for size in asteroids:
        while stack and size < 0 and stack[-1] > 0:
            diff = size + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                size = 0
            else:
                size = 0
                stack.pop()
        if size:
            stack.append(size)
    
    return stack

if __name__ == '__main__':
    # Test Case 1
    asteroids = [5,10,-5]
    print(asteroidCollision(asteroids))

    # Test Case 2
    asteroids = [8,-8]
    print(asteroidCollision(asteroids))

    # Test Case 3
    asteroids = [10,2,-5]
    print(asteroidCollision(asteroids))