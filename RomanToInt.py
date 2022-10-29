class RomanToInt:
    def romanToInt(self, s: str) -> int:
        #create dictionary
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
		
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
		
        res = 0
        for c in s:
            res += values[c]
            
        return res
