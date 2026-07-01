class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps the number to its index
        seen = {}
        
        for index, value in enumerate(nums):
            complement = target - value
            
            # Check if the needed number was already seen
            if complement in seen:
                return [seen[complement], index]
            
            # Record the current number and its index
            seen[value] = index
