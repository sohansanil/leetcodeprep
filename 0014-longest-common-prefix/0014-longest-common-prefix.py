class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len= min(len(words) for words in strs)
        s=""
        for i in range(min_len):
            current = strs[0][i]
            for j in range (len(strs)):

                if  current != strs[j][i] :
                    return s
            s += current


        return s       
