class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mp={}
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
        for key,value in mp.items():
            if value > (n//2) :
                return key
        return -1       
