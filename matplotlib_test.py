#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('sample.csv')
#%%
x = df['x']
y = df['y']
#%%
#横軸をx、縦軸をyの散布図（scatter）をプロット
plt.scatter(x, y)
plt.show()
#%%
#データの概要を表示
df.describe()
#%%
df.mean()
#%%
#中心化
df_c = df - df.mean()
#%%
df_c.head(3)
#%%
df_c.describe()
#%%
#データの抽出
x = df_c['x']
y = df_c['y']
#%%
plt.scatter(x, y)
plt.show()
#%%
xx = x * x
#%%
xy = x * y
#%%
a = xy.sum() / xx.sum()
#%%
a
#%%
plt.scatter(x, y ,label = 'y') #実測値
plt.plot(x, a * x, label = 'y_hat', color = 'red') #予測値
plt.legend() #凡例の表示
plt.show()
#%%
#予測値の計算
x_new = 40
#%%
mean = df.mean()
#%%
mean['x']
#%%
#中心化
xc = x_new - mean['x']
#%%
xc
#%%
#単回帰分析による予測
yc = a * xc
#%%
yc
#%%
#元のスケールの予測値
y_hat = a * xc + mean['y']
#%%
y_hat
#%%
#予測値を計算する関数の作成
def predict(x):
    #定数項
    a = 10069.022519284063
    xm = 37.62222
    ym = 121065.0
    #中心化
    xc = x - xm
    #予測値の計算
    y_hat = a * xc + ym
    return y_hat
#%%
#予測値
predict(40)
#%%
predict(30)
#%%
predict(50)