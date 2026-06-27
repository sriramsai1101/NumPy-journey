import numpy as np
arr=np.arange(1,101)
even=arr[arr%2==0]
print(even)
print(even.size)

brr=np.arange(1,101)
odd=brr[brr%2==1]

print(odd)
print(odd.size)
print(even.sum())
