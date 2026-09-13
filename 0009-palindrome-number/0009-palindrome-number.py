class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        original_x = x
        ans = 0
        
        # 3. Reverse the number mathematically
        while x > 0:
            rem = x % 10
            ans = ans * 10 + rem
            x = x // 10
            
        # 4. Compare the original with the reversed version
        return original_x == ans