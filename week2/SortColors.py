


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]>nums[y]:
                    nums[x],nums[y]=nums[y],nums[x]
        return nums            

    # nums=list(map(int,input().split()))    
    # print(sortColors(1,nums))    