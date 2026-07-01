class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        for i in strs:
            ele = "".join(sorted(i))
            if ele in dictt:
                dictt[ele].append(i)

            else:
                dictt[ele] = [i]

        res=[]
        for key, value in dictt.items():
            res.append(value)

        return res
