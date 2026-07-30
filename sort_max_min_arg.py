import numpy as np
arr=np.array([
    [12,45,18],
    [67,23,90],
    [34,81,56]
])
print(np.max(arr))
print(np.min(arr))
print(arr[arr>40])
print(arr[arr%2==0])
print(np.sort(arr))
