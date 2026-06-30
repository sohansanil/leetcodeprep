class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        
        vowel_count = sum(1 for c in s[:k] if c in vowels)
        max_count = vowel_count

      
        for i in range(k, len(s)):

            
            if s[i-k] in vowels:
                vowel_count -= 1

            
            if s[i] in vowels:
                vowel_count += 1

            max_count = max(max_count, vowel_count)

        return max_count