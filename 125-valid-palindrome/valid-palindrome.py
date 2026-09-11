class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(filter(str.isalnum,s)).lower()
        if c[::-1] == c:
            return True

        return False