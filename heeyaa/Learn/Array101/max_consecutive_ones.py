from typing import List

# ========Answer Part ========
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, result = 0, 0
        
        for num in nums:
            if num == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
                
        return result
# =============================


if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    obj = Solution()
    print(obj.findMaxConsecutiveOnes(nums))