class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]>nums[y]:
                    nums[x],nums[y]=nums[y],nums[x]
        for x in range(len(nums)):
            if nums[x]==target:
                ans.append(x)            
        return ans 
    nums=list(map(int,input().split())) 
    target=int(input())   
    print(targetIndices(1,nums,target)) 