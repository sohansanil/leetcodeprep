class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        e = len(s) - 1
        
        while st < e:
            # Skip non-alphanumeric characters from the left
            while st < e and not s[st].isalnum():
                st += 1
            
            # Skip non-alphanumeric characters from the right
            while st < e and not s[e].isalnum():
                e -= 1
                
            # Compare the characters (make them both lowercase first!)
            if s[st].lower() != s[e].lower():
                return False
            
            # Move both pointers inward for the next check
            st += 1
            e -= 1
            
        return True