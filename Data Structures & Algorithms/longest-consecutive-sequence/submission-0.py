class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest_streak = 0
        
        for num in sett:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in sett:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in sett:
                    current_num += 1
                    current_streak += 1
                    
                # Update the maximum streak
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak



