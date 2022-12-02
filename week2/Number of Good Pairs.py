class Solution:
    def numIdenticalPairs(self, l: list[int]) -> int:
            count=0
            for x in range(len(l)):
                for y in range(x+1,len(l)):
                    if l[x]==l[y]:
                        count+=1
            return(count)            
            
# l=list(map(int,input().split()))
# print(goodPairs(l))    