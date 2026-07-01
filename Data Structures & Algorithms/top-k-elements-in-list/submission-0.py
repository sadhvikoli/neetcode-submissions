class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        sorted_keys = sorted(my_dict, key=my_dict.get)

        res = []
        for _ in range(k):
            res.append(sorted_keys.pop())

        return res


