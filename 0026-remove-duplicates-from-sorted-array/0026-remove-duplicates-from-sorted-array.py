class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        writer = 1
        for explorer in range(1, len(nums)):
            
            
            if nums[explorer] != nums[explorer - 1]:
                
                
                nums[writer] = nums[explorer]
                
                
                writer += 1
                
   
        return writer