import numpy as np
arr=np.random.randint(1,100,(5,5))
print(arr)
print(arr.shape)
print(arr.size)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))

print(arr[arr>50])