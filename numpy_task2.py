import numpy as np
marks=np.array([
    [80,75,90,88],
    [70,60,55,78],
    [10,20,30,40]
])
sum =marks.sum(axis=0)
print("total marks: ", sum)
print("average marks :",np.mean(sum))
print("highest marks:",np.max(sum))
print("lowest marks:",np.min(sum))
print(np.argmax(sum))
print(np.argmin(sum))
