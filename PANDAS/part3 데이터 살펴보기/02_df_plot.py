# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('남북한발전전력량.xlsx', engine='openpyxl')  # 데이터프레임 변환 

df_ns = df.iloc[[0, 5], 3:]            # 남한, 북한 발전량 합계 데이터, 1991이후 만 추출
df_ns.index = ['South','North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경
print(df_ns.head())
print(df_ns.values.dtype)              # df_ns 변환전 데이터타입 확인
print(df_ns.columns.values.dtype)       # df_ns.columns 변환후 데이터타입 확인
print('\n')


#%%
# 선 그래프 그리기
df_ns.plot()

# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()


#%%
# 북한합계만 데이터 뺴오기
df_n = df.iloc[[5], 3:]
df_n.index = ['North']
df_n.columns = df_n.columns.map(int)
print(df_n)

df_n.plot()  # 행 열이 이상해서 그림이 이상하게나옴 

# 행열 전치해서 다시
tdf_n = df_n.T
tdf_n.plot()

#%% 
# 다양한 종류의 그래프를 그리고싶으면 뒤에 (kind= '')를 붙이면됨
# bar
tdf_ns.plot(kind='bar')

#%%
# 히스토그램 - 데이터값을 범주용으로 활용하여 나타냄
# 바로 plot()하면 에러가남
# TypeError: no numeric data to plot

# 자료형 변환
tdf_ns = tdf_ns.astype(int)

tdf_ns.plot(kind='hist')


#%%
# scatter: 산점도 - 분포도를 확인하는데 사용
# 2개의 열을 선택하여 그림

# read_csv() 함수로 df 생성
df = pd.read_csv('auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 차의 중량과 연비의 관계
df.plot(x='weight',y='mpg', kind='scatter')  # 중량이 커질수록 연비가 낮아짐
tdf_ns.plot(kind='scatter')

#%% 
# boxplot: 박스플롯 - 주식에서 주로 사용 
#  이상치가 있을떄 주로 사용

# read_csv() 함수로 df 생성
df = pd.read_csv('auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 열을 선택하여 박스 플롯 그리기
df[['mpg','cylinders']].plot(kind='box')

