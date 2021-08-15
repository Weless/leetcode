from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res =  {1}
        for i in range(len(primes)-1):
            res.add(primes[i])
            j = i+1
            while j < len(primes) - 1:
                res.add(primes[j])

