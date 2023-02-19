class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            step += 1
        return step
s = Solution
assert(s.numberOfSteps(s, 14) == 6)
assert(s.numberOfSteps(s, 8) == 4)
assert(s.numberOfSteps(s, 123) == 12)