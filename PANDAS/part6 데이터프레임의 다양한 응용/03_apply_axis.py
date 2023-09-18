# 함수 매핑
# apply(axis=):  
#  데이터프레임의 각 열에 함수 매핑 => apply(axis=1)
# 데이터프레임의 각 행에 함수 매핑 => apply(axis=0)


import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
 
# 사용자 함수 정의  
missing_value_cnt = 0

def missing_value(series):    # 시리즈를 인수로 전달
    global missing_value_cnt 
    missing_value_cnt += 1
    return series.isnull()    # 불린 시리즈를 반환 
    


# 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환
result = df.apply(missing_value, axis=0)  #기본값 axis=0  ∵ result = df.apply(missing_value) 와 같음
print(result.head())
print('\n')
print(type(result))

print("총 함수 호출 회수: ", missing_value_cnt)  # 2번 
#  axis=0이라서 각 칼럼단위로 2번(age, fare) 호출 
# axis = 1이면은 891번 호출

#%%
# 최대값 최소값

# 사용자 함수 정의
def min_max(x):    # 최대값 - 최소값
    return x.max() - x.min()
    
# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환
result = df.apply(min_max,  axis=0)   #기본값 axis=0 
print(result)
print('\n')
print(type(result))



#%%
# 2개의 열을 합친 새로운열 만들기(01.apply에서 문제로 했음)

# 사용자 함수 정의
def add_two_obj(a, b):    # 두 객체의 합
    return a + b

# 데이터프레임의 2개 열을 선택하여 적용
# x=df, a=df['age'], b=df['fare'] 
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['fare']), axis=1)   
# 굳이 람다쓰는데 함수를 넣어?
asd = df.apply(lambda x : x['age'] + x['fare'], axis=1)   
print(df.head())



