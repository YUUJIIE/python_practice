#%%
import pandas as pd
#%%
#CSVファイルの読み込み
df = pd.read_csv('sample.csv')
#%%
df.head(3)
#%%
#データの抽出
x = df['x']
y = df['y']
#%%
