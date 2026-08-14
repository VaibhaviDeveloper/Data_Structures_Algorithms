# a=[1,5,2,6,0,4,3]
 # print("Before Partitioning :" , str(a))
# left=-1
# n=len(a)
# key=a[n-1]

# for i in range(n-1):
 #   if a[i]<=key:
  #      left+=1
  #      a[i],a[left] = a[left],a[i]

# left+=1
# a[left],a[n-1]=a[n-1],a[left]

#print("After partitioning:" , str(a))


a = [100,34,76,35,57,23,98,37,69,143]

def QuickSort(a):
    if len(a) <= 1:
       return a
    mid=len(a)//2
    pivot=a[mid]
    lesser=[x for x in a if pivot > x]
    greater =[x for x in a if pivot < x]
    return QuickSort(lesser)+[pivot]+QuickSort(greater)

a=QuickSort(a)
print(a)