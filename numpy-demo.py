import numpy as np

print("1.数组创建")

arr1 = np.array([1,2,3,4,5])
arr2 = np.arange(0,5,2)

matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(f"数组:{arr1}")
print(f"数组序列arr2：{arr2}")
print("矩阵")
print(matrix)

print("2.切片操作")
print(f"数组切片arr1[1,5]:{arr1[1:5]}")
print(f"arr1[1,5,2]:{arr1[1:5:2]}")
print(f"矩阵第二行：{matrix[1]}")
print(f"矩阵第二列：{matrix[:,1]}")
print(f"子矩阵：{matrix[0:2,1:3]}")


print("3.矩阵四则运算")
a = np.array([1,2,3])
b = np.array([4,5,6])
print(f"a+b:{a+b}")
print(f"a-b:{a-b}")
print(f"a*b:{a*b}")
print(f"a@b:{a@b}")
print(f"a/b:{a/b}")

print("4.统计运算")
data = np.array([2,4,6,8,10])
print(f"平均值：{data.mean()}")
print(f"最大值：{data.max()}")
print(f"最小值：{data.min()}")
print(f"方差：{data.var()}")
print(f"标准差：{data.std()}")

print(f"矩阵每一列均值：{matrix.mean(axis = 0)}")
print(f"矩阵每一行均值：{matrix.mean(axis = 1)}")

print(f"元素平方：{data**2}")

