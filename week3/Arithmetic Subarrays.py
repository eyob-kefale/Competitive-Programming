class Solution:
    def checkArithmeticSubarrays(self, m: list[int], l: list[int], r: list[int]) -> list[bool]:       
       

        ans=[]

        for x in range(len(r)):
            p=[]
            for y in range(l[x],r[x]+1):
                p.append(m[y])
            p=sorted(p)
            k=p[1]-p[0]
            e=True
            for y in range(1,len(p)):
                if p[y]-p[y-1]!=k:
                    e=False
                    break  
            ans.append(e) 
        return(ans)         
