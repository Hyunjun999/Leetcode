class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]