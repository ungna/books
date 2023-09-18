# -*- coding: utf-8 -*-

# 데이터 표준화
# 

# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# 각 열의 자료형 확인
print(df.dtypes)   


#%%
# horsepower 열의 고유값 확인
# 고유값 = 중복되지 않는 값들
print(df['horsepower'].unique())

#%%
# 누락 데이터('?')라고 표기한거 삭제 
import numpy as np

df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
# dropna를 사용해 nan을 지움 근대 ?도 nan으로 바꿔서 ?까지 지운효과
df.dropna(subset=['horsepower'], axis=0, inplace=True)   
# horsepower 열의 자료형 확인
print(df['horsepower'].dtypes)  

#%%
# 숫자인데 obj로 표기되있음 실수로 바꾸자
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# horsepower 열의 자료형 확인
print(df['horsepower'].dtypes)  

#%%
# origin 열의 고유값 확인
print(df['origin'].unique())  # [1 3 2]

#%%
# origin에 있는 1 3 2 들의 개수를 카운트
# origin의 unique에 index로 번호 넣기위해 카운트로 unique를 뽑아냄
origin_counts = df['origin'].value_counts()
origin_index = origin_counts.index

print(origin_index)
#%%
# ?? 왜함 ??
origin_values = origin_index.values

#%%
# 뽑아낸걸 series로 타입변환
origin_series = pd.Series(origin_values)

#%%
# 정수형 데이터를 문자형 데이터로 변환
# 1 2 3 대신 나라이름 넣음
df['origin'].replace({1:'USA', 2:'EU', 3:'JAPAN'}, inplace=True)

# origin 열의 고유값과 자료형 확인
print("uninque:", df['origin'].unique())   # ['USA' 'JAPAN' 'EU']
print("dtype:", df['origin'].dtypes)     # object


#%%
# 유한개의 고유값을 반복적으로 나타내면 범주형으로 표기하는게 좋음
# origin 열의 문자열 자료형을 범주형으로 변환
df['origin'] = df['origin'].astype('category')     
print(df['origin'].dtypes) 

# 다시 objeect로 돌아가고싶으면
# df['origin'] = df['origin'].astype('str')


#%%

# model year 열 타입확인
print(df['model year'].sample(3))  # Name: model year, dtype: int64

# model year 열의 정수형을 범주형으로 변환
df['model year'] = df['model year'].astype('category') 

# model year 열 타입확인
print(df['model year'].sample(3))   # Categories (13, int64): [70, 71, 72, 73, ..., 79, 80, 81, 82]