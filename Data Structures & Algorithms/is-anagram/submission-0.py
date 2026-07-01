class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictt={}
        for i in s:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i] = 1

        for i in t:
            if i in dictt:
                dictt[i]-=1
            else:
                return False

        for key, value in dictt.items():
            if value != 0:
                return False

        return True
