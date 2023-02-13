// 각 원소의 배수를 계산한 후, 오름차순으로 정렬
// #include <vector>
// #include <algorithm>

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // 배수 계산
        for(int i = 0; i <nums.size(); i++) {
            nums[i] *= nums[i];
        }
        // 오름차순 정렬 (vector와 sort함수)
        sort(nums.begin(), nums.end());
        
        return nums;
    }
};

//runtime:40ms, memory usage:25.7mb