from typing import List
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1 : return 0
        isPrimes = [1] * n
        ans = 0
        isPrimes[0],isPrimes[1] = 0,0
        for i in range(2, int(n**0.5)+1):
            if isPrimes[i] == 1:
                j = i*i
                while j<n:
                    isPrimes[j] = 0
                    j+=i
        for i in isPrimes:
            if i == 1:
                ans +=1
        return ans

