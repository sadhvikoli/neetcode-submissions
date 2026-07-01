class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sset = set()
        for i in nums:
            if i in sset:
                return True
            else:
                sset.add(i)

        return False