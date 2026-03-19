# -*- coding: utf-8 -*-
# @Time    : 2026/3/19
# @Author  : 马建彤
# @File    : 01_matrix_operation.py
# @Desc    : 使用 NumPy 实现矩阵的加减乘除运算

import numpy as np

# 1. 定义两个 2x2 矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("矩阵 A：")
print(A)
print("\n矩阵 B：")
print(B)

# 2. 矩阵加法
C = A + B
print("\n矩阵加法 (A + B)：")
print(C)

# 3. 矩阵减法
D = A - B
print("\n矩阵减法 (A - B)：")
print(D)

# 4. 矩阵乘法（点乘）
E = np.dot(A, B)  # 或 A @ B
print("\n矩阵乘法 (A × B)：")
print(E)

# 5. 矩阵转置
A_T = A.T
print("\n矩阵 A 的转置：")
print(A_T)
