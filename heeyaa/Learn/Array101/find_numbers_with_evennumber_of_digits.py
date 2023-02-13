from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        result = 0
        
        for num in nums:
            if self.numOfDigits(num) %2 == 0:
                result += 1
        return result
            
            
    ##숫자 자릿수 세주는 함수
    def numOfDigits(self, num:int) -> int:
        if num == 0:
            return 1
        digits = 0
        
        while num != 0:
            num //= 10
            digits += 1
        return digits
            

if __name__ == "__main__":

    solution = Solution()
    print(solution.findNumbers([12,345,2,6,7896]))