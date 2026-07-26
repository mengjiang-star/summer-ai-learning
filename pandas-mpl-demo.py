import pandas as pd
import matplotlib.pyplot as plt

# 1.构造简易数据集（模拟AI训练数据集）
data = {
    "姓名":["张三","李四", "王五", "赵六", "钱七", "孙八"],
    "分数": [88, 76, 92, 59, 84, 95],
    "年龄": [20, 21, 20, 22, 21, 20]
}

# 转换成表格结构
df = pd.DataFrame(data)
print("==原始完整数据表==")
print(df)

# 基础表格操作
print("\n==查看前三行数据==")
print(df.head(3))

print("\n==查看基础信息==")
print(df.info())

print("\n==统计数值列均值、最值 describe()====")
print(df.describe())

# 数据筛选
high_score = df[df["分数"] > 80]
print("\n==筛选：分数>80 的学生==")
print(high_score)

filter_data = df[(df["年龄"] == 20) & (df["分数"] > 85)]
print("\n==筛选：20岁且分数大于85==")
print(filter_data)

score_col = df["分数"]
print("\n====单独提取分数列====")
print(score_col.values)

# Matplotlib 数据可视化 
# 解决Windows中文乱码问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ①折线图姓名-分数
plt.figure(figsize=(8,4))
plt.plot(df["姓名"], df["分数"], marker="o", label="学生分数")
plt.title("学生成绩折线图")
plt.xlabel("学生姓名")
plt.ylabel("分数")
plt.legend()
plt.savefig("score_line.png")
print("\n✅ 折线图已保存 score_line.png")

# ②散点图：年龄-分数分布
plt.figure(figsize=(6,4))
plt.scatter(df["年龄"], df["分数"], color="orange", s=60)
plt.title("年龄-分数分布散点图")
plt.xlabel("年龄")
plt.ylabel("分数")
plt.savefig("score_scatter.png")
print("✅ 散点图已保存 score_scatter.png")