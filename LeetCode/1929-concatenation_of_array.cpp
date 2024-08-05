#include <iostream>
#include <vector>

using namespace std;

vector<int> getConcatenation(vector<int>& nums) {
    int n = nums.size();

    vector<int> result(2 * n);

    for (int i = 0; i < n; i++){
        result[i] = nums[i];
        result[i + n] = nums[i];
    }

    return result;
}

int main() {
    vector<int> nums{ 1, 2, 3 };
    vector<int> result = getConcatenation(nums);
    
    for (int i = 0; i < result.size(); i++){
        cout << result[i] << "\n";
    }

    return 0;
}