t=int(input())
while t:
    n=int(input())
    div=0
    ans=0
    for x in range(n,n+6):
        if x%5==0:
            div=x
            break
    if div-n<3 and n>=38:
        n=div 
    print(n)
               
    t-=1