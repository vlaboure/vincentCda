import numpy as np

a = [1, 2, 3]
print(a)
arr = np.array(a)
print(arr)
test = np.arange(10, 0, -1)
print(test * test)
test2d = test.reshape(2, 5)
print(test2d)
# test2 = np.arange(10)
# test2.shape
testresize = np.resize(test, (2, 3))
print(testresize)

tranche = test[5:]
print(tranche)
print(test2d[0, :])
for row in test2d:
    print(row, type(row))
c1, c2 = test2d
print(c1, c2)
