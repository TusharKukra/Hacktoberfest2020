t=int(input())
for j in range(1,t+1):
    n=int(input())
    v=list(map(int,input().split()))
    r=0
    m=-1
    for i in range(n):
        if(v[i]>m and ((i==n-1) or (v[i]>v[i+1]))):
            #print(v[i])
            r+=1
        m=max(m,v[i])
    print('Case #'+str(j)+': '+str(r))
