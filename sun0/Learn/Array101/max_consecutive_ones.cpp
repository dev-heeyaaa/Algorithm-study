class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;
        for (int a : nums) {
            if (a == 1) {
                count ++;
                // max함수로 최대값 비교
                maxCount = max(maxCount, count);
            }
            else {
                count = 0;
            }
        }
        return maxCount;
    }
};

// runtime:47ms, memoryusage: 36.2mb