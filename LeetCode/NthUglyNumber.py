class Solution(object):
    # O(log(INT_MAX)) Time | O(log(max(a, b, c)))
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        left = 1
        right = 2000000000
        while left <= right:
            mid = left + (right - left)/2
            result = self.uglyNumbersAvailable(a, b, c, mid)
            if n < result:
                right = mid - 1
            elif n > result:
                left = mid + 1
            else:
                if mid % a == 0 or mid % b == 0 or mid % c == 0:
                    return mid
                else:
                    right = mid - 1                   
        return -1
        
    def uglyNumbersAvailable(self, a, b, c, target):
        result = target/a 
        ab = self.getLCM(a, b)
        bc = self.getLCM(b, c)
        ac = self.getLCM(a, c)
        abc = self.getLCM(self.getLCM(a, b), c)
        result -= target/ab
        result -= target/ac
        result -= target/bc
        result += target/abc
        return result + target/b + target/c
            
        
    def getLCM(self, a, b):
        return a * b / self.getGCD(a, b)
    
    def getGCD(self, a, b):
        if b == 0:
            return a
        return self.getGCD(b, a % b)
    
