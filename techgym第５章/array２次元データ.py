import numpy as np

# 2x3の行列を作成
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 行列の内容を表示
print("2次元配列:")
print(matrix)

# 特定の要素にアクセス
element = matrix[1, 2]  # 2行目、3列目の要素にアクセス
print(f"要素 (2行目、3列目): {element}")
