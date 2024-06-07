
from functools import reduce
import operator

class Solution:
    def factor(self, num: int)->int:
        fact=[]
        while num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    num = num // i
                    fact.append(i)
                    break
        return fact
        
    def firstContact(self, n : int, m : int) -> int:
        n = self.factor(n)
        m = self.factor(m)
        for number in m:
            if number in n:
                n.remove(number)
        m = m + n
        tot = 1
        return reduce(operator.mul, m, 1)
        
            
        


        
sol = Solution()
m = sol.factor(8)
n = sol.factor(52)

for number in m:
    if number in n:
        n.remove(number)
m = m+n
tot = reduce(operator.mul, m, 1)
print(tot)
#