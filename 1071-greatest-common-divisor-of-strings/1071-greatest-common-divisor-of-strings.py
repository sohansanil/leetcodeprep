from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:




        if str1 + str2 == str2 + str1:
            g = gcd(len(str1), len(str2))

            ans = str1[:g]
            return ans

        else:
            return ""    
        