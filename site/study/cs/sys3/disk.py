# import math
li=[65,67,98,122,124,183,37,14]
sum=0
for i in range(1,len(li)):
    sum+=abs(li[i]-li[i-1])
print(sum)