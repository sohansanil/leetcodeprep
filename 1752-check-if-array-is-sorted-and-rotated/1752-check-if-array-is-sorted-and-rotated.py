class Solution:
    def check(self, nums: list[int]) -> bool:
        drop_count = 0
        n = len(nums)
        
        
        for i in range(n):
           
            if nums[i]>nums[(i+1)%n]:
                drop_count += 1
            
          
            if drop_count > 1:
                return False
                
       
        return True