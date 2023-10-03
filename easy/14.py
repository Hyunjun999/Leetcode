class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = []
        min_len = len(sorted(strs, key=lambda x: len(x))[0])
        for i in range(min_len):
            l = list(map(lambda x: x[: i + 1], strs))

            if all(e == l[0] for e in l):
                res.append(l[0])
        return "" if len(res) == 0 else res[-1]


# Return the longest common prefix in strs
sol = Solution()
assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["c", "acc", "ccc"]) == ""
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
