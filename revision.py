#2d array

import numpy as np

numbers=np.array([
  [  [10,20,30],
    [50,60,70],
    [40,80,90]
  ],
  [
      [24,25,26],
      [34,35,36],
      [43,45,47]
  ]
    ])
print("arrays",numbers)
print("arrays*2",numbers*2)
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
print(numbers[0])
print(numbers.shape)
print(numbers.size)
arr=np.zeros((3,3))
print(arr)
ones=np.ones((3,3))
print(ones)
arr=np.arange(1,100,2)
print(arr)
points=np.linspace(0,10,5)
print(points)
rand=np.random.randint(0,100,6)
print(rand)
rand=np.random.randint(0,100,(2,3))
print("random matrix ",rand)
deci=np.random.rand(5)
print(deci)
arr1=[10,32,42]
arr2=[11,13,23]
total=np.concatenate((arr1,arr2))
print(total)

print("m" ,numbers[0,:])