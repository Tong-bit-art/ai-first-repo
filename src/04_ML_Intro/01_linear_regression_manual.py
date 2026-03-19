# -*- coding: utf-8 -*-
# @Time    : 2026/3/19
# @Author  : 马彤
# @File    : 01_linear_regression_manual.py
# @Desc    : 手动实现一元线性回归（最小二乘法，不使用sklearn）

import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 1. 生成模拟数据 ----------------------
# 假设真实关系：y = 2*x + 3 + 噪声
np.random.seed(42)  # 固定随机种子，保证结果可复现
x = np.linspace(0, 10, 100)  # 生成 0~10 之间的 100 个点
y = 2 * x + 3 + np.random.normal(0, 1, size=len(x))  # 加高斯噪声

print("数据预览（前5个）：")
print("x:", x[:5])
print("y:", y[:5])

# ---------------------- 2. 最小二乘法计算参数 ----------------------
# 公式：
# w = (n*Σ(xi*yi) - Σxi*Σyi) / (n*Σ(xi²) - (Σxi)²)
# b = (Σyi - w*Σxi) / n

n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# 计算斜率 w 和截距 b
w = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - w * sum_x) / n

print(f"\n计算得到的模型参数：")
print(f"斜率 w = {w:.4f}")
print(f"截距 b = {b:.4f}")
print(f"拟合直线：y = {w:.4f}x + {b:.4f}")

# ---------------------- 3. 用模型进行预测 ----------------------
y_pred = w * x + b

# ---------------------- 4. 可视化结果 ----------------------
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="blue", label="原始数据（带噪声）", alpha=0.6)
plt.plot(x, y_pred, color="red", linewidth=2, label=f"拟合直线：y = {w:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("手动实现一元线性回归（最小二乘法）")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# ---------------------- 5. 计算模型评估指标 ----------------------
# 均方误差 MSE
mse = np.mean((y - y_pred) ** 2)
# 决定系数 R²（越接近1越好）
ss_total = np.sum((y - np.mean(y)) ** 2)
ss_residual = np.sum((y - y_pred) ** 2)
r2 = 1 - (ss_residual / ss_total)

print(f"\n模型评估：")
print(f"均方误差 MSE = {mse:.4f}")
print(f"决定系数 R² = {r2:.4f}")
