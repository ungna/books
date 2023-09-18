# 판다스
# conda activate ENV   (내가만든 가상환경의 이름)
# pip install pandas

import pandas as pd


# Series (1차원)
# dict와 비슷하지만 key:value 가 아니라 index:value 형식을 가진다
# 그래서 dict을 시리즈로 변환하는 방식을 많이 사용한다
# 프린트할때마다 젤밑에 dtype: ~ 가 뜸

# dict 생성
dict_data = {"a":1, "b":2, "c":3}

# pandas.Series() 로 series형식으로 변환. sr에 저장
sr = pd.Series(dict_data)

print(type(sr))    #  <class 'pandas.core.series.Series'>
print(sr)
"""  출력하면 이렇게 나옴:
        a    1
        b    2
        c    3
        dtype: int64    # dtype은 시리즈를 구성하는 데이터값의 자료형이 int64라는 뜻이다
"""
        
#%%

# list를 시리즈로 변환하기

# list생성
list_data = [ '2023-09-01', 3.14, 'ABC', 100, True]

# series로 변환
sr2 = pd.Series(list_data)
print(type(sr2))
print(sr2)
"""  출력하면 이렇게 나옴:  
# 인덱스에 default로 정수형index 번호가뜸  
# values는 list에 입력한 값
       0    2023-09-01
       1          3.14
       2           ABC
       3           100
       4          True
       dtype: object
"""

#%%
# 인덱스, 값만 뽑기
print("index:", sr2.index)   # index: RangeIndex(start=0, stop=5, step=1)  # default는 range형식으로 보여줌 
print("values:", sr2.values)

#%%

# 튜플을 시리즈로 변환하기
tuple_data = ('unggna', '2023-09-01', '남', True)

# series로 변환
# default말고 인덱스를 지정해보기: 값의 갯수와 순서를 일치시켜야됨   # 리스트도됨
sr = pd.Series(tuple_data, index=['이름', '생년월일', '성별', '학생여부'])

print(type(sr))   
print(sr)

print("--" * 10)
print("index:", sr2.index)  
print("values:", sr2.values)


#%% 
# seires 슬라이싱
# 접근방법이 2가지가있음
# []    value만 나옴

# 1. 인덱스로 접근
print(sr['이름'])
print(sr.loc['이름'])

# 2. default번호로 접근
print(sr[0])       # 권고하지 않음  밑에 지저분하게 뜸
print("")
print(sr.iloc[0])  # 권고

#%%
# 범위지정 슬라이싱 :  [ : ]
# index value 둘다 나옴
print("[0:3]:", "\n", sr.iloc[0:3])
print("[1:2]:", "\n", sr.iloc[1:2])
print("['이름':'성별']:", "\n", sr['이름': '성별'])



# 몇개만 골라서 슬라이싱 :  [[ , , ]]
## [[]]    index value 둘다 나옴
print("[0, 1, 3]:", "\n", sr2[[0, 1, 3]])

# 튜플은 안됨
# print("['이름','성별']:", "\n", sr[['이름', '성별']])
# KeyError: 'key of type tuple not found and not a MultiIndex'



