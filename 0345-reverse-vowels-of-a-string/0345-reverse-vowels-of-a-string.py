class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','A','E','e','i','I','o','O','u','U']

    
        l=list(s)
        left = 0
        right = len(s)-1
        while left<right:
            if l[left] not in vowels:
                left+=1
            elif l[right] not in vowels:
                right-=1

            else:

                l[left],l[right]= l[right],l[left]
                left+=1
                right-=1

        return "".join(l)    

        "".join(l)                  