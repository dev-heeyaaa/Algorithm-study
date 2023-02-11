from typing import List

# ==================Answer Part =================
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squares_list = [pow(num, 2) for num in nums]
        result = sorted(squares_list)
        
        return result
#==================================================

if __name__ == "__main__":
    obj = Solution()
    print(obj.sortedSquares([-7,-3,2,3,11]))