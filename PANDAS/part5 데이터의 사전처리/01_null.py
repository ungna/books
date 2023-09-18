# null: 누락 데이터 처리

import seaborn as sns

# titanic 데이터셋 가지고오기
df = sns.load_dataset('titanic')

#%%
# df 데이터 구경하기
df.columns  # 항목이 뭐있는지
df.index    # 몇개있는지

df.head()  # 맨 앞에 x개 # default: 5
df.tail(10)  # 맨 뒤에 10개

print(df.info())  # 전체적인 데이터 확인  # index, Column, Non-Null Count, Dtype  

#%%
# deck 열의 NaN 개수 계산하기
# dropna = False쓰면은 nan값개수까지 나옴 # dropna = True쓰면은 nan값은 버리고 값있는거만 나옴
nan_deck = df['deck'].value_counts(dropna=False)  
print(nan_deck)

#%%
# isnull() 메서드로 누락 데이터 찾기
# null 이면 True 값이있으면 False
print(df.isnull())
print(df.head().isnull())   # 앞에 5개만 isnull확인

#%%
# isnull() 누락데이터 개수구하기
print(df.isnull().sum)  # 데이터 전체를 보여줌 (사실상 sum안넣은거나 다름없음)
print(df.isnull().sum(axis=0)) # column별로 모아서 보여줌
print(df.isnull().sum(axis=1)) # index별로 모아서 보여줌

#%%
# notnull() 메서드로 누락 데이터 찾기
# null이 있으면은 False 값이 있으면 True  - isnull과 반대
print(df.head().notnull())



#%%
# 누락 데이터 제거
# isnull로 nan 데이터 찾음
missing_df = df.isnull()

# for로 각 열의 NaN 개수 계산하기 
# 걍 print(df.isnull().sum(axis=0)) 써도 됨 결과 똑같음
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()    # 각 columns의 NaN 개수 파악

    try:    # missing_count가 없으면 에러뜨니까 그때 exceot로 0을 출력  # 에러때문에 if못씀
        print(col, ': ', missing_count[True])   # True 즉, NaN 값이 있으면 개수를 출력
    except:
        print(col, ': ', 0)                     # NaN 값이 없으면 0개 출력

#%%
# dropna - nan값이 있는 데이터 제거
"""
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
axis : {0: index / 1: columns} 결측치 제거를 진행 할 레이블입니다.
how : {'any' : 존재하면 제거 / 'all' : 모두 결측치면 제거} 포함만 시켜도 제거할지, 전부 NA여야 제거할지 정함
tresh : 결측값이 아닌 값이 몇 개 미만일 경우에만 적용시키는 인수 입니다.
예를들어, tresh값이 3이라면 결측값이 아닌 값이 3개 미만일 경우에만 dropna메서드를 수행합니다.
subset : dropna메서드를 수행할 레이블을 지정합니다. ex) subset = age면 age에서 nan가 있을때 수행
inplace : 원본을 변경할지의 여부입니다.
https://wikidocs.net/153202
"""
# NaN 값이 500개 이상인 column을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh_500 = df.dropna(axis=1, thresh=500)  
print(df_thresh_500.columns)

# age 열에 나이 데이터가 없는 모든 index을 삭제 - age 열(891개 중 177개의 NaN 값)
df_age = df.dropna(subset=['age'], how='any', axis=0)  
print(len(df_age))

#%%
# dropna  - subset
df_all = df.dropna(subset=['age'], how='all', axis=0)  
print(len(df_all))  # 714  조건에 age밖에없으니 age만 nan이있으면 삭제됨

df_all = df.dropna(subset=['age', 'sex'], how='all', axis=0)  
print(len(df_all))  # 891   조건에 age, sex중에 둘다 nan이 있어야되는데 sex는 전부 정해져서 하나도 삭제 안됨


#%%
# 누락데이터 치환: fillna()
# 누락된걸 원하는 데이터로 넣기 (평균값 구해서 넣어보자)

df = sns.load_dataset('titanic')

# age 열의 평균 계산 (NaN 값 제외)
mean_age = df['age'].mean(axis=0)  # mean_age = df['age'].mean() 도 가능

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
df['age'].fillna(mean_age, inplace=True)

# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값이 평균으로 대체)
print(df['age'].head(10))

#%%
# fillna().idxmax() 
# 가장 많이 나온걸로 넣기

df = sns.load_dataset('titanic')

# embark_town 열의 829행의 값이 NaN
print(df['embark_town'][825:830])
print('\n')

# idxmax()로 승선도시 중에서 가장 많이 출현한 값 넣음
# value_counts(dropna=True)) # Southampton 644 Cherbourg 168 Queenstown 77 
# value_counts(dropna=False)) # Southampton 644 Cherbourg 168 Queenstown 77 NaN 2   # NaN까지 카운트
most_freq = df['embark_town'].value_counts(dropna=True).idxmax() # dropna=True 면은 NaN은 제외하고 카운트
print(most_freq)
print('\n')

df['embark_town'].fillna(most_freq, inplace=True)

# embark_town 열 829행의 NaN 데이터 출력 (NaN 값이 most_freq 값으로 대체)
print(df['embark_town'][825:830])


#%%
# fillna(method='ffill', inplace=True)
# NaN값에 바로 앞에있는걸로 채워넣기(excel 셀병합 한거 채울때 주로 씀)

df = sns.load_dataset('titanic')

# embark_town 열의 829행의 값이 NaN
print(df['embark_town'][825:830])
print('\n')

# embark_town 열의 NaN값을 바로 앞에 있는 828행의 값으로 변경하기
# df['embark_town'].fillna(method='ffill', inplace=True)  # 곧 사라진다고함
df['embark_town'].ffill(inplace=True)      # 권장
print(df['embark_town'][825:830])

