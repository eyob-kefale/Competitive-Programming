class Solution:
    def smallerNumbersThanCurrent(self, l: list[int]) -> list[int]:       
        ans=[]
        for x in range(len(l)):
            cnt=0
            for y in range(len(l)):
                if l[x]>l[y]:
                    cnt+=1
            ans.append(cnt)
        return ans            
        
            

        