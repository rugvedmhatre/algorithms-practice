/*

https://leetcode.com/problems/find-the-difference-of-two-arrays/

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.


Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and 
nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and 
nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], 
their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].


Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000

*/
# include <vector>
# include <set>
# include <iostream>

using namespace std;

vector<vector<int> > findDifference(vector<int>& nums1, vector<int>& nums2) {
    set<int> nums1Set(nums1.begin(), nums1.end());
    set<int> nums2Set(nums2.begin(), nums2.end());

    vector<int> result1, result2;

    for (int num : nums1Set){
        if (nums2Set.count(num) == 0) {
            result1.push_back(num);
        }
    }

    for (int num : nums2Set){
        if (nums1Set.count(num) == 0) {
            result2.push_back(num);
        }
    }

    return {result1, result2};
}

int main(){
    // Test Case 1
    vector<int> nums1 = {1,2,3};
    vector<int> nums2 = {2,4,6};

    vector<vector<int> > result1 = findDifference(nums1, nums2);

    for (vector<int> vec : result1){
        for (int num : vec){
            cout << num << " ";
        }
        cout << endl;
    }

    // Test Case 2
    vector<int> nums3 = {1,2,3,3};
    vector<int> nums4 = {1,1,2,2};

    vector<vector<int>> result2 = findDifference(nums3, nums4);

    for (vector<int> vec : result2){
        for (int num : vec){
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}