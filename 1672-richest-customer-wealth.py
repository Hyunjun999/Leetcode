class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = []
        for acc in accounts:
            wealth.append(sum(acc))
        return max(wealth)
s = Solution
assert(s.maximumWealth(s, [[1,2,3],[3,2,1]]) == 6)
assert(s.maximumWealth(s, [[1,5],[7,3],[3,5]]) == 10)
assert(s.maximumWealth(s, [[2,8,7],[7,1,3],[1,9,5]]) == 17)
print('Success!')