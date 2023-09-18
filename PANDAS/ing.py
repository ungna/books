import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
df['ten'] = 10
#%%
# def사용
def tot(x):
    return  x['age'] + x['fare'] + x['ten']

df['tot'] = df.apply(tot, axis = 1)

# lambda사용
df['tot_lambda'] = df.apply(lambda x : x['age'] + x['fare'] + x['ten'], axis = 1)

#%%
# x[]안쓰고 for안에 넣어서

def tot_cols(x):
    sum = 0
    for i in x:
        print(i)
        sum = sum + i
    return sum

total =  df.apply(tot_cols, axis = 1)
df['total'] = total




#%%
import pandas as pd

sum = pd.Series()

for i in df.columns:
    print(i)
#%%
df = df.drop('total', axis=1)

#%%
def tot_index(x):
    tot = []
    for i in range(0, 891):
        t = x.iloc[i]
        print(type(t))
    return pd.Series(tot)

total =  df.apply(tot_index, axis = 1)


#%%
df.iloc[0].values  # <class 'numpy.ndarray'> # array([22.  ,  7.25, 10.  , 39.25, 39.25])

#%%
import pandas as pd

# df의 각 index값들을 시리즈로 바꿈
# .sum()이 안되서 바꾸는거
a = pd.Series(df.iloc[0].values)

#%%
# 시리즈로 바꾼index의 합을 구함
a.sum()

#%%
