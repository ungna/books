# -*- coding: utf-8 -*-
# 범주형 데이터 처리
# bin: 일정한 구간으로 나누어서 처리 why? 히스토그램으로 표기하기위해서

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열의 ? 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      
df.dropna(subset=['horsepower'], axis=0, inplace=True)   
df['horsepower'] = df['horsepower'].astype('float')     


#%%
# bin으로 나누기
# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기
# 정확히 3개의 bin크기가 같음
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

print(bin_dividers) # [ 46.   107.33333333     168.66666667    230.  ]

# 46~170.333   170.333~168.667  168.667~230 이렇게 3구간으로 나뉜거임

# np.histogram 안하고 걍 list로 값넣고 만들어도됨
# bin_dividers = [46, 100, 200, 230]  # 이런식으로 기준을 만들어서 할수있음

# 나눈 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

#%%
# pd.cut 함수로 각 데이터를 3개의 bin에 할당
# hp_bin이라는 새 column을 값을 넣어서 추가함
# cut(x, bins, right=True, labels=None, retbins= 'False , precision: 'int'=3, include_lowest=False, duplicates: 'str'='raise', ordered=True)
df['hp_bin'] = pd.cut(x=df['horsepower'],     # 데이터 배열 - 기준이 되는 데이터
                      bins=bin_dividers,      # 경계 값 리스트
                      labels=bin_names,       # bin 이름
                      include_lowest=True)    # 첫 경계값 포함(이상)  # false로하면 초과

#%%
# horsepower 열, hp_bin 열의 첫 15행을 출력
print(df[['horsepower', 'hp_bin']].head(15))


#%%
# dummy variables
# 하지만 이런 범위는 머신러닝 알고리즘에 적용못함 (컴퓨터가 인식 못해서) -> 인식가능한 더미변수를 사용해야됨
# 용도: 원핫인코딩(one-hot-encoding)

# hp_bin 열의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head())

"""
  저출력  보통출력  고출력
0   False   True  False      # 보통
1   False   True  False      # 보통
2   False   True  False     # 보통
3   False   True  False     # 보통
4   False   True  False     # 보통
5   False  False   True     # 고출력

# 하나만 true고 나머지는 false로 표기
"""


#%%

# 히스토그램 만들어보기
import pandas as pd

df['horsepower'].plot(kind='hist', bins=3)
# np.histogram(df['horsepower'], bins=3) 으로 했을때 나온 값이 그래프로나옴 
# count에 y값(몇개있는지)이 bin_divider에 x값(값이 나눠지는거)이 들어감