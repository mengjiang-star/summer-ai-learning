# AI库测试 Demo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1.Numpy 数组运算
arr = np.array([1, 2, 3, 4, 5])
print("Numpy数组：", arr)
print("数组平均值：", arr.mean())

# 2.Pandas 表格数据
data = {
    "姓名": ["张三", "李四", "王五"],
    "分数": [86, 92, 78]
}
df = pd.DataFrame(data)
print("\nPandas表格：")
print(df)

# 3.Matplotlib 绘图，保存图片
x = [1,2,3,4,5]
y = [2,4,1,5,3]
plt.plot(x,y, label="测试曲线")
plt.legend()
plt.savefig("result.png")
print("\n绘图完成，已生成 result.png")