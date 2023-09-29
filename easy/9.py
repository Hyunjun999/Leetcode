class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == '-':
            return False
        l, r = 0, len(s) - 1
        while True:
            if l == r or l > r:
                return True
            elif s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                return False