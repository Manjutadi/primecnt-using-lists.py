import math as m
def cp(n,data):
    h=0
    for i in data:
        cnt=0
        if i==2 or i==3 or i==5:
            cnt=0
        k=int(m.sqrt(i))
        for j in range(2,k+1):
            if i%j==0:
                cnt+=1
                break
        
        if cnt==0:
            h+=1
    return h       
