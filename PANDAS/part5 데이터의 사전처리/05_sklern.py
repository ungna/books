# -*- coding: utf-8 -*-
# sklern: 머신러닝 라이브러리
# sklern을 이용한 원핫인코딩 처리
# 원핫인코딩: 숫자 0,1 또는 True, False로 데이터를 변환

import pandas as pd
import numpy as np

# 앞에서 한거

df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열의 ? 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      
df.dropna(subset=['horsepower'], axis=0, inplace=True)   
df['horsepower'] = df['horsepower'].astype('float')     

# bin 3개로 나누기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

print(bin_dividers) # [ 46.   107.33333333     168.66666667    230.  ]

# 나눈 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],     # 데이터 배열 - 기준이 되는 데이터
                      bins=bin_dividers,      # 경계 값 리스트
                      labels=bin_names,       # bin 이름
                      include_lowest=True)    # 첫 경계값 포함(이상)  # false로하면 초과


#%%%

# sklern 라이브러리 불러오기
from sklearn import preprocessing    

# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()       # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성


#%%
# label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))  
print(onehot_labeled)      # [1 1 1 1 1 0 0 0 0 0 0 1 1 0 2]
print(type(onehot_labeled))   # <class 'numpy.ndarray'>


#%%
# 2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) 
print(onehot_reshaped)  # 리스트 형태로 변환
print(type(onehot_reshaped))  # <class 'numpy.ndarray'>


#%%
# 희소행렬로 변환 
# 15 * 1 형태의 행렬
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))  # <class 'scipy.sparse._csr.csr_matrix'>




"""
희소 행렬(Sparse Matrix)은 행렬의 원소 중에 많은 항들이 '0'으로 구성되어 있는 행렬이다. 
희소 행렬의 대부분의 항은 '0'으로 이루어져 있어, 실제 사용하지 않는 메모리 공간으로 인해 
메모리 낭비가 발생하게 된다. 그러나 0 값을 제외하고 0이 아닌 값(비영 요소)만 따로 추출하여 
새로운 배열로 구성하는 방법을 사용함으로써 메모리를 효율적으로 사용할 수 있다.

ex)  배열의 '0행'에는 <전체 행의 개수, 전체 열의 개수, 추출한 원소의 개수> 값을 삽입한다.

int arr={6, 5, 5,  # <6행, 5열, 0이아닌거 5개>
         0, 0, 3,  # (0,0)에 3이 들어가있음
         2, 2, 4,  # (2,2)에 4가 들어있음 ... 
         3, 3, 2,   
         4, 0, 9,
         5, 4, 1}

위를 풀어내면 이렇게 나옴:
3 0 0 0 0 
0 0 0 0 0 
0 0 4 0 0 
0 0 0 2 0 
9 0 0 0 0 
0 0 0 0 1
"""

