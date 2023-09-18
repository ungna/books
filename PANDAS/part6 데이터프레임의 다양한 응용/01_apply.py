# 함수 매핑
# 시리즈 또는 데이터프레임의 개별 원소, 객체를 특정 함수에 일대일 대응시키는 과정
"""
1-1 개별 원소에 함수 매핑
 시리즈 원소에 함수 매핑  => apply
 데이터프레임 원소에 함수 매핑 => applymap

1-2 시리즈 객체에 함수 매핑
 데이터프레임의 각 열에 함수 매핑 => apply(axis=1)
 데이터프레임의 각 행에 함수 매핑 => apply(axis=0)

1-3 데이터프레임 객체에 함수 매핑  =>pipe 
"""
# apply()
# 시리즈 원소에 함수 매핑

import seaborn as sns


# titanic 데이터셋에서 age, fare 2개 열을 선택해 데이터프레임으로 만듬
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())

# 사용자 함수 정의
def add_10(n):
    return n + 10

def add_two_obj(a,b):
    return a + b

# apply()를 이용해 시리즈 객체에 적용
sr1 = df['age'].apply(add_10)    # n=df['age']의 모든 원소
print(sr1.head())

# 시리즈 객체에 적용: 2개의 인수
sr2 = df['age'].apply(add_two_obj, b=10)  # a=df['age']의 모든 원소, b=10
print(sr2.head())

# def 말고 lambda 사용가능
sr3 = df['age'].apply(lambda x : x + 10)  # x=df['age'] 
print(sr3.head())


#%%
# [문제] 칼럼: age, ten을 apply함수로 전달하여 age+ten의 결과를
# ageten이라는 칼럼을 만들어서 넣어라

import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')

# 사용자 함수 정의
def add_two_obj(a, b):
    return a + b

# age_ten 데이터프레임의 크기가 (891,891)이라서 바로 안넣어짐
age_ten = df['age'].apply(add_two_obj, b = df['ten'])  # 방법1

# 이렇게 하니까 크기가 (891,)로됨 = series가 됨
df['age_fare'] = df[['age']].apply(add_two_obj, b = df['fare'])  # 방법2 

df['age_ten'] = age_ten[0]   # 방법1 
# 방법2는 바로 column으로 넣을수 있어서 위처럼 안해도됨
print(df['age_ten'].head())
#%%
# 방법3
ageten = df.apply((lambda x : x['age'] + x['ten']), axis = 1)  # axis = 1을 넣어서 index별로 넣음
df['ageten'] = df.apply((lambda x : x['age'] + x['ten']), axis = 1)

# apply안쓰고 쉽게 하는법:
sr = df
sr['age_ten'] = sr.age + sr.ten
sr['age_fare'] = sr.age + sr.fare

#%%
# 방법 1에 def 수정본

def add_two_obj(a, b):
    c = a + b
    return c[0] 

df['age_ten3'] = df['age'].apply(add_two_obj, b = df['ten'])

# 방법3 def로 추가
def add_lamb(n):
    return n['age']+n['ten']

a = df.apply(add_lamb, axis=1)
df['a'] = df.apply(add_lamb, axis=1)

#%%

def add_all(*args):
    return sum(args)

# 이렇게 하니까 df['age'].apply(add_all) ,  a = df[ten'].apply(add_all)
# 이렇게 2번 따로따로 처리되서 args가 전부 안합쳐짐
a = df[['age','ten']].apply(add_all)

#%%

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
lll = df.fare[5]  # == df['age'][0]
