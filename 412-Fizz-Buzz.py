class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 != 0:
                res.append('Fizz')
            elif (i + 1) % 3 != 0 and (i + 1) % 5 == 0:
                res.append('Buzz')
            elif (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                res.append('FizzBuzz')
            else:
                res.append(str(i + 1))
        return res
s = Solution
assert(s.fizzBuzz(s, 3) == ["1","2","Fizz"])
assert(s.fizzBuzz(s, 5) == ["1","2","Fizz","4","Buzz"])
assert(s.fizzBuzz(s, 15) == ["1","2","Fizz","4","Buzz","Fizz",
                             "7","8","Fizz","Buzz","11","Fizz",
                             "13","14","FizzBuzz"])
print('Success!')