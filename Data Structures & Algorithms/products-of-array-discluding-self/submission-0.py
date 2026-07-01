class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Calculate prefix products (left to right)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Multiply with suffix products (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res

