a=[0,0,1,0,2,2,0,1,1,0,0,2]

def Sorting(a):
    n=len(a)
    i=0
    j=n-1
    while(i<=j):
        if(a[i]==0):
            i+=1
        elif(a[j]==1 or a[j]==2):
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    print(i)
    print(j)

Sorting(a)
print(a)

