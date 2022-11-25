class Solution(object):
    def fizzBuzz(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        s=int(s)
        for x in range(1,s+1):
            if x%3==0 and x%5==0:
                l.append("FizzBuzz")
            elif x%3==0:
                l.append("Fizz")
            elif x%5==0:
                l.append("Buzz")
            else:
                x=str(x)
                l.append(x) 
        return l    
    print(fizzBuzz(2,15))