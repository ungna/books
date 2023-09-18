# 시계열 데이터(timestamp, period)
# Timestamp를 쓰는이유: 다른 형식의 날짜라도 Timestamp로 바꾸면 똑같은 포맷으로 맞출 수 있다.
# 시간, 날짜로 관리하면 시간순서에 맞춰 인덱싱 슬라이싱하기 편해진다
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

import pandas as pd

# read_csv() 함수로 CSV 파일을 가져와서 df로 변환
df = pd.read_csv('stock-data.csv')

# 데이터 내용 및 자료형 자료형 확인
print(df.head())
print('\n')
print(df.info())

# 문자열 데이터(시리즈 객체)를 Timestamp로 타입변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열(cloumn)로 추가
## 굳이 새로 new_Date 만들어서 할필요 없이 바로 덮어씌우면됨
## df['Date'] = pd.to_datetime(df['Date'])  

# 데이터 내용 및 자료형 확인
print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))  # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(df['new_Date'].dtype)     # datetime64[ns]

#%%
# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)

## 덮어씌운걸 바로 index로 변환
## df.set_index('Date', inplace=True)

# 데이터 내용 및 자료형 자료형 확인
print(df.head())
print('\n')
print(df.info())



#%%
# Period는 어떤 기간을 나타냄 
# Timestamp는 딱 그 시점, 어떤 특정한 시간을 나타낸다.


# Period
# 날짜 형식의 문자열로 구성되는 리스트 정의
dates = ['2019-01-01', '2020-03-01', '2021-06-01']

# 시계열 데이터(Timestamp)로 변경
new_date = pd.to_datetime(dates)

# Timestamp를 period 데이터로 변경
# period는 MS, QS, B 등은 안먹힘
pr_day = new_date.to_period(freq='D') # 년-월-일
print(pr_day)
pr_month = new_date.to_period(freq='M') # 년-월
print(pr_month)
pr_year = new_date.to_period(freq='Y') # 연도
print(pr_year)
pr_yearq = new_date.to_period(freq='Q') # 연도Q1234
print(pr_yearq)      # PeriodIndex(['2019Q1', '2020Q1', '2021Q2'], dtype='period[Q-DEC]')

# freq옵션의 종류
""" 
D(1일), W(1주), M(월말), MS(월초), Q(분기말), QS(분기초), 
A(연말), AQ(연초), B(휴일 제외), H(1시간), T(1분), S(1초)
"""

#%%
# date_range(): timestamp 배열만들기
# 1달단위, MS
ts_month = pd.date_range(start = '2019-01-01',  # 시작할 날짜
                         end = None,         # 끝나는 날짜
                         periods = 6,        # 생성할 timestamp수
                         freq='MS',         # 시간간격 MS:월초
                         tz='Asia/Seoul'  # timezone: 시간대
                         )
print("ts_month:", ts_month) 

# 3단단위, M
ts_3month = pd.date_range(start = '2019-01-01',
                          end = None,     # None안하고 딴거쓰니까 자꾸 안됨
                          periods = 4,
                          freq='3M',    # 시간간격 M:월말
                          tz = 'Asia/Seoul'
                          )
print("ts_3month:", ts_3month) # 근대 3개월 단위인데 처음은 19-01-31으로 시작함

#%%
# period_range(): 여러 peroid(기간)이 들어있는 데이터를 만들기

# Period 배열 만들기 - 1개월 길이
pr_month = pd.period_range(start='2019-01-01',     # 날짜 범위의 시작
                   end=None,                   # 날짜 범위의 끝
                   periods=3,                  # 생성할 Period 개수
                   freq='M')                   # 기간의 길이 (M: 월)
print(pr_month)

# Period 배열 만들기 - 1시간 길이
pr_hour = pd.period_range(start='2019-01-01',    
                   end=None,                   
                   periods=3,                  
                   freq='H')             # 기간의 길이 (H: 시간)
print(pr_hour)


# Period 배열 만들기 - 2시간 길이
pr_2hour = pd.period_range(start='2019-01-01',  
                   end=None,                   
                   periods=3,               
                   freq='2H')
print(pr_2hour)



#%%
# datetime(dt): 날짜데이터 분리

import pandas as pd

df = pd.read_csv('stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   

# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
# n = df['new_Date'].dt  # 했을때 n의 Variable Explorer를 확인하면 
# year month에서 Series라고뜸 - Series형태로 만든다는거
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())


#%%
# datetime(dt) 인덱싱
# 날짜 인덱스를 이용하여 데이터 선택하기

import pandas as pd

df = pd.read_csv('stock-data.csv')

# 문자열을 날짜로 바꾸고 인덱스 설정
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace = True)

# 날짜 인덱스를 이용하여 데이터 선택하기
df_y = df.loc['2018']     # loc 인덱서 활용
print(df_y.head())

df_ym = df.loc['2018-06']    # loc 인덱서 활용
print(df_ym.head())


# loc를 사용해 index에서 2018-06 , column에서 start~high까지 슬라이싱
df_ym_cols = df.loc['2018-06', 'Start':'High']    # 열 범위 슬라이싱
print(df_ym_cols)

df_ymd = df.loc['2018-07-02']
print(df_ymd)

# 날짜인덱스 개별적으로 조회
df_ymds = df.loc[['2018-06-25','2018-06-20']]    
print(df_ymds)

# 날짜 슬라이싱
# df_ymd_range = df.loc['2018-06-25' : '2018-06-20']   # 슬라이싱에 loc안먹음
# df_ymd_range = df['2018-06-25':'2018-06-20']         # 이것도 안되네
df_ymd_range = df[  # 날짜범위지정
                  pd.to_datetime('2018-06-25') : 
                  pd.to_datetime('2018-06-20')]


print(df_ymd_range)
#%%

# 시간 간격 계산. 
today = pd.to_datetime('2018-12-25')      # 기준일 생성
df['time_delta'] = today - df.index       # 날짜 차이 계산하고 column에 추가

# 행 인덱스로 지정
df.set_index('time_delta', inplace=True)    
# 최근 180일 ~ 189일 사이의 값들만 선택하기  # 위에는 안됬는데 이건 되네 
df_180 = df['180 days':'189 days']
print(df_180)