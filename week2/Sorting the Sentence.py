class Solution:
    def sortSentence(self, l: str) -> str:  
        
        l=l.split()   
        d=[]
        ans=""
        for x in range(1,len(l)+1):
            for y in range(len(l)):
                if str(x) in l[y]:
                    d.append(l[y])
        w=[]            
        for x in range(1,len(d)+1):
            w.append(x)
        for x in range(len(d)):
            for y in range(len(d[x])):
                if d[x][y]!=str(x+1):
                    ans+=d[x][y]
                elif d[x][y]==str(x+1) and x<len(d)-1:
                    ans+=" "   
                    break
                else:
                    break
                    
        return (ans)    
      