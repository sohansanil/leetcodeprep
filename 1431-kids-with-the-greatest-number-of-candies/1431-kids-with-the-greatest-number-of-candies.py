class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer=[]
        max_candies= max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies: 
                answer.append(True)
            else:
                answer.append(False)
        return answer

        