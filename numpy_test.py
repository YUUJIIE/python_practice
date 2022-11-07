#%%
import numpy as np
#%%
x = np.array([1, 2, 3])
#%%
x
#%%
y = np.array([2, 3.9, 6.1])
#%%
#平均の算出
x.mean()
#%%
y.mean()
#%%
#中心化
xc = x - x.mean()
#%%
xc
#%%
yc = y - y.mean()
#%%
yc
#%%
#要素ごとの掛け算（要素積）
xx = xc * xc
#%%
xx
#%%
xy = xc * yc
#%%
xy
#%%
xx.sum()
#%%
xy.sum()
#%%
a = xy.sum() / xx.sum()
#%%
a