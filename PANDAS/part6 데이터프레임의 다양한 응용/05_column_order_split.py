# -*- coding: utf-8 -*-


import pandas as pd
import seaborn as sns

### 열 순서변경
# titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']

# 열 이름의 리스트 만들기
columns = list(df.columns.values)   #기존 열 이름
print(columns, '\n')

# 열 이름을 알파벳 순으로 정렬하기
columns_sorted = sorted(columns)    #알파벳 순으로 정렬
df_sorted = df[columns_sorted]
print(df_sorted, '\n')

# 열 이름을 기존 순서의 정반대 역순으로 정렬하기
columns_reversed = list(reversed(columns))  
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

# 열 이름을 사용자가 정의한 임의의 순서로 재배치하기
columns_customed = ['pclass', 'sex', 'age', 'survived']  
df_customed = df[columns_customed]
print(df_customed)

# 데이터셋 가져오기
df = pd.read_excel('./주가데이터.xlsx', engine= 'openpyxl')
print(df.head(), '\n')
print(df.dtypes, '\n')



#%%
### split
# 연, 월, 일 데이터 분리하기
# 문자열로 변환해서 

# 문자열 메소드 사용을 자료형 변경
df['연월일'] = df['연월일'].astype('str')  

# 문자열을 split() 메서드로 분리
dates = df['연월일'].str.split('-')    # - 기준으로 나눔
print("쪼갠거 확인: \n", dates.head())

# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
df['연'] = dates.str.get(0)     # dates 변수의 원소 리스트의 0번째 인덱스 값
df['월'] = dates.str.get(1)     # dates 변수의 원소 리스트의 1번째 인덱스 값 
df['일'] = dates.str.get(2)     # dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head())


#%%
# 연, 월, 일 데이터 분리하기 
# timestamp타입으로 변환해서

# timestamp로 자료형 변환
dates = pd.to_datetime(df['연월일'])
# dt를 사용해 분리
df_y = dates.dt.year
df_m = dates.dt.month
df_d = dates.dt.day

# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
df['연'] = df_y
df['월'] = df_m
df['일'] = df_d