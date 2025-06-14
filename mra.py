#%%
#行列演算の基礎
#ベクトルの定義
#行列の定義
#転置の計算
#逆行列の計算
#行列積
import numpy as np
#%%
#ベクトルの定義　
x = np.array([[1],[2],[3]])
print(x)
#%%
#行列の定義
X = np.array([[1,2], [3,4]])
print(X)
#%%
#転置
Xt = X.T
print(Xt)
#%%
#逆行列
#linear algebra: 線形代数
X_inv = np.linalg.inv(X)
print(X_inv)
#%%
#行列積
XX_inv = np.dot(X, X_inv)
print(XX_inv)
#%%
#ベクトルを定義するときは二重括弧で囲う
x = np.array([[1, 2, 3]])
x
#%%
x.T
#%%
#Numpyでよく使う処理
X = np.array([
    [2, 3, 4],
    [1, 2 ,3]
])
#%%
print(X)
#%%
X.shape
#%%
row, col = X.shape
#%%
row
#%%
col
#%%
for x in X:
    print(x)
    print('--------')