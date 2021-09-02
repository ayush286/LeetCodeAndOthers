class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output = ""
        reverseString = ""
        asIsString = ""        
        for index in range(len(s)):
            if len(asIsString) == k:
                output += asIsString
                asIsString = ""
            if len(reverseString) == k:
                reverseString = self.getReverseString(reverseString)
                output += reverseString
                reverseString = ""
                
            x = index % (2 * k)
            if x >= k:
                asIsString += s[index]
            else:
                reverseString += s[index]
        if len(asIsString) > 0:
            output += asIsString
        if len(reverseString) > 0:
            reverseString = self.getReverseString(reverseString)
            output += reverseString
        return output
            
    def getReverseString(self, reverseString):
        return reverseString[::-1]
