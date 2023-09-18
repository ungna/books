# 판다스
# conda activate ENV   (내가만든 가상환경의 이름)
# pip install pandas

# 데이터프레임: DataFrame
# 2차원 배열, 행렬
# 여러개의 시리즈들이 한데 모여서 이룸 like 엑셀
# 딕셔너리 안에 values값을 리스트로 만들어서 데이터프레임으로 변환하는 방식을 주로씀

import pandas as pd

# dict
dict_data = {
    'c0': [1, 2, 3],     # 칼럼, 시리즈
    'c1': [4, 5, 6],     # 칼럼, 시리즈
    'c2': [7, 8, 9],     # 칼럼, 시리즈
    'c3': [10, 11, 12],    # 칼럼, 시리즈
    'c4': [13, 14, 15]     # 칼럼, 시리즈
}

# 데이터프레임으로 변경
fd = pd.DataFrame(dict_data)

print(type(fd))    # <class 'pandas.core.frame.DataFrame'>
print(fd)


# values 안에 list의 길이가 같아야됨
"""
dict_data = {
    'c0' : [1, 2, 3],    
    'c1' : [4, 5, 6],  
    'c2' : [7, 8, 9], 
    'c3' : [10, 11, 12],  
    'c4' : [13, 14, 15, 16]  # 혼자 4개있으면은 에러
    }
# ValueError: All arrays must be of the same length
"""


# %%
# default 인덱스는 숫자, column은 키이름으로 나옴
print(fd)

"""
   c0  c1  c2  c3   c4
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
"""

# %%

# 리스트를 데이터프레임에 넣기
# 리스트를 데이터프레임에 넣으려면 리스트 안에 리스트로 2차원으로 만들어야됨
data = [
    [15, '남', '팔달고'],
    [17, '여', '장안고']
]

# 리스트에 넣기  선언하면서 이름을 행,열넣음
# 리스트는 key가 없어서 columns을 처음 선언할때 넣어도됨
df = pd.DataFrame(data,
                  index=['철수', '영희'],
                  columns=['나이', '성별', '학교']
                  )

print(df)
"""
    나이 성별   학교
철수  15  남  팔달고
영희  17  여  장안고
"""


# %%
# 행, 열에 이름 넣어주기


# 처음 선언할때 index만 넣음 colums를 넣으면은 안됨 값을 못찾아서 내용들이 NaN이뜸
# dict만 그럼 리스트는 columns에 이름넣고 선언해도됨
fd = pd.DataFrame(dict_data, index=['1st', '2nd', '3rd'])

print(fd)
"""
   c0  c1  c2  c3   c4
1st  1  4  7  10  13
2nd  2  5  8  11  14
3rd  3  6  9  12  15
"""
#%%

# 나중에 이름 부여하기
fd.index = ['이름', '성별', '나이']
fd.columns = ['일', '이', '삼', '사', '오']

print(fd)
"""
    일  이  삼   사   오
이름  1  4  7  10  13
성별  2  5  8  11  14
나이  3  6  9  12  15
"""

# 행, 열 이름을 일부만 변경  inplace=True 넣어야됨
fd.rename(index={'이름': 'name'}, inplace=True)   # '이름'을 'name'으로 바꿈
fd.rename(columns={'일': 'one'}, inplace=True)   # '일'을 'one'으로 바꿈
print(fd)

#%%

# 행, 열 삭제
# 행(index)삭제 : axis = 0
# 열(column)삭제 : axis = 1

print(fd)

# 행삭제
fd0 = fd.drop('name', axis = 0)
print(fd0)


# 열삭제
fd1 = fd.drop('one', axis = 1)
print(fd1)

# 굳이 axis =  안써도 되는데 그럼 이름 같은거 있으면 다 지울수 있어서 쓰는게 안전
# 'name' axis = 1 하면 에러남  why? 열에 name이 없어서  
# KeyError: "['name'] not found in axis"