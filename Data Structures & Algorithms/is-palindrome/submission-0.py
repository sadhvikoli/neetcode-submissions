class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([i for i in s.lower() if i.isalnum()])
        return cleaned == cleaned[::-1]

