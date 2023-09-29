class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]
    
s = Solution
assert(s.runningSum(s, [1,2,3,4]) == [1,3,6,10])
assert(s.runningSum(s, [1,1,1,1,1]) == [1,2,3,4,5])
assert(s.runningSum(s, [3,1,2,10,1]) == [3,4,6,16,17])