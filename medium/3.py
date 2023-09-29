class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longer = 0
        i, j = 0, 0
        char = set()
        while j < len(s):
            if s[j] not in char:
                char.add(s[j])
                j += 1
                longer = max(longer, j - i)
            else:
                char.remove(s[i])
                i += 1
        return longer


# Given a string s, return the length of the longest substring
# without repeating characters.

sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
