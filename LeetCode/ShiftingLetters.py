class Solution(object):
    # O(n) Time | O(n) Space where n is length of shifts
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        sumFromLeft = [0 for number in range(len(shifts))]
        sumFromLeft[0] = shifts[0]
        totalSum = shifts[0]
        for index in range(1, len(shifts)):
            sumFromLeft[index] = sumFromLeft[index - 1] + shifts[index]
            totalSum += shifts[index]
        totalShifts = [0 for number in range(len(shifts))]
        totalShifts[0] = totalSum
        for index in range(1, len(shifts)):
            totalShifts[index] = totalSum - sumFromLeft[index - 1]
        shiftString = ""
        for index in range(len(s)):
            shiftString += self.getShiftedLetter(s[index], totalShifts[index])
        return shiftString
    
    
    def getShiftedLetter(self, char, shift):
        shift %= 26
        newAscii = ord(char) + shift
        if newAscii > 122:
            newAscii -= 26
        return chr(newAscii)
