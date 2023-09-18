# duplicate: 중복 데이터 처리
# bool 형태로 나옴: 중복이면 T  아니면 F

import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)

# 데이터프레임 전체 index 데이터 중에서 중복값 찾기
# 바로앞의 행(index)과 비교해 중복되면은 True가 나온다
df_dup = df.duplicated()
print(df_dup)

"""
  c1  c2  c3
0  a   1   1     F  # 비교대상이 없으니 무조건 F나옴
1  a   1   1     T
2  b   1   2     F
3  a   2   2     F
4  b   2   2     F
"""

# 데이터프레임의 특정 index 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)

""" c2 기준으로 중복값찾음 
c2  
1    F
1    T
1    T
2    F
2    T
"""

#%%
# drop_duplicates(): 중복 행을 제거
# 중복되는 행을 제거하고 고유관측값을 가진 행들만 남는다
df2 = df.drop_duplicates()
print(df2)
"""
  c1  c2  c3
0  a   1   1
1  a   1   1  # 얘가 사라짐 (a,1,1)중복
2  b   1   2
3  a   2   2
4  b   2   2
"""

# c2, c3열을 기준으로 중복 행을 제거
df3 = df.drop_duplicates(subset=['c2', 'c3'])  # 2 2 중에서 먼저나온 a 와 함께 조합된게 남음
print(df3)

"""
  c1  c2  c3
0  a   1   1
1  a   1   1  # 얘가 사라짐 (1,1)중복
2  b   1   2
3  a   2   2
4  b   2   2  # 얘가 사라짐 (2,2)중복
"""