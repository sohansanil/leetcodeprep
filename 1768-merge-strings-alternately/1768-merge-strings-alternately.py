class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer=""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            answer+=word1[i]
            answer+=word2[i]
            
        answer+= word1[min_len:]    
        answer+= word2[min_len:] 
        return answer
        

        