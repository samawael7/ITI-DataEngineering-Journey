import numpy as np

# 1
numarray = np.arange(10,51,5)
print(numarray)

# 2
zeroarr = np.zeros((4,6))
zeroarr[2] = 99
print(zeroarr)

# 3
arr = np.array([12, 45, 7, 19, 88, 3, 56, 91, 24, 67])
print(arr[arr > 50])

# 4
a = np.eye(5)
np.fill_diagonal(a, [10,20,30,40,50])
print(a)

# 5
x = np.arange(1,21).reshape(4,5)
# A
print(x[-2:]) 
# B
print(x[:,2]) 
# C
print(x[:3,2:])

# 6
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

result = a*b + (a+b)
print(result)


# 7
data = np.array([150, 200, 90, 300, 100, 450])
normalized = (data - data.min()) / (data.max() - data.min())
print(normalized)


# 8
standardized = (data - data.mean()) / data.std()
print(standardized)


# 9
mat = np.array([
    [7,3,12],
    [11,9,6],
    [4,20,15],
    [15,0,14]
])

print(mat.mean(axis=1))
print(mat.sum(axis=0))

max_val = mat.max()
pos = np.unravel_index(mat.argmax(), mat.shape)
print(max_val, pos)


# 10
a = np.arange(1,11)
a[1:4] = 99
print(a)


# 11
arr = np.arange(1,17).reshape(4,4)
print(arr[::-1, ::-1])


# 12
ages = np.array([23,45,19,34,28,51,17,39])
names = np.array(["Ali","Sara","Omar","Lina","Khaled","Nour","Yara","Hassan"])

print(names[(ages >= 25) & (ages <= 40)])


# 13
ages[ages < 20] = 20
print(ages)


# 14
np.random.seed(123)
rand_arr = np.random.randint(1,101,(6,6))
print(rand_arr)


# 15
nums = np.random.normal(100,15,7)
print(nums)


# 16
colors = np.array(["red","blue","green","yellow","purple"])
print(np.random.choice(colors,4,replace=False))


# 17
nums = np.arange(1,21)
np.random.shuffle(nums)
print(nums)