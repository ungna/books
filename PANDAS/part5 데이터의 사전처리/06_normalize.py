# 정규화(06_normalize.py): 숫자 데이터의 상대적 크기차이를 제거
# 각 열의 데이터값을 동일한 크기 기준으로 나눈 비율로 나타냄
# 데이터의 범위: 0 ~ 1  또는 -1 ~ 1

import pandas as pd
import numpy as np


df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']  

# horsepower 열의 ? 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      
df.dropna(subset=['horsepower'], axis=0, inplace=True)  
df['horsepower'] = df['horsepower'].astype('float')

#%%
# 최소값: ?  ~ 최대값 : 1
#  통계 요약정보(describe)로 최대값(max)을 확인
print(df.horsepower.describe())

# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
df["horsepower_max"] = df.horsepower / abs(df.horsepower.max()) 

print(df.horsepower_max.head())
print('\n')
print(df.horsepower_max.describe())

#%%
# 최소값: 0 ~ 최대값 : 1
# horsepower 열의 통계 요약정보로 최대값(max)과 최소값(min)을 확인
print(df.horsepower.describe())
print('\n')

# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
min_x = df.horsepower - df.horsepower.min()  # 데이터 전체에 최소값을 뺴서 최소값을 0으로 만듬
min_max = df.horsepower.max() - df.horsepower.min()  # 최대값에 최소값을 뺀 값을 만듬
df['horsepower_minmax'] = min_x / min_max     # 최소가 0인거(전체에 최소뺀거) / 최대에서 최소뺸거

print(df.horsepower_minmax.head())
print('\n')
print(df.horsepower_minmax.describe())

#%%
#######그래프로 만들어보기#####

import seaborn as sns
import matplotlib.pyplot as plt

# max

ax = sns.distplot(df['horsepower_max'], 

                      hist=True,   # 막대
                      kde=False,    # 곡선  # 근대 곡선이 멀 나타내는지 모르겠음
                      bins=8, 
                      color='blue', 
                      hist_kws={'edgecolor': 'gray'},  # 막대표시
                      kde_kws={'linewidth': 1})        # 곡선표

ax.set_title('max')
ax.set_xlabel('horsepower')
ax.set_ylabel('frequency')
ax.xlim(0.0, 1.0)  # x의 범위 설정

plt.show(ax)

#%%

# minmax
ax = sns.distplot(df['horsepower_minmax'], 

                      hist=True,   # 막대
                      kde=False,
                      bins=8, 
                      color='blue', 
                      hist_kws={'edgecolor': 'gray'},  # 막대표시
                      )        

ax.set_title('minmax')
ax.set_xlabel('horsepower')
ax.set_ylabel('frequency')
ax.xlim(0.0, 1.0)  # x의 범위 설정

plt.show(ax)


#%%
# 두개 합치기
plt.subplot(211)

plt.plot(t1, f(t1))
plt.plot(t1, f(t1))
