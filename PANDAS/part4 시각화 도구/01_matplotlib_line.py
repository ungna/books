
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib은 파이썬 표준 시각화 도구라고 할정도로 많이 쓰인다
# 선 그래프 : matplotlib.pyplot

# matplotlib은 한글폰트 오류문제 해결
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임으로 변환
df = pd.read_excel('시도별 전출입 인구수.xlsx', engine='openpyxl', header = 0)

# 병합한거를 이해못해서 누락값(NaN)으로 넣음 (엑셀 양식 병합 부분)
# NaN을 앞 데이터로 채워야됨 
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] !='서울특별시')
df_seoul = df[mask]  # True에 해당하는 데이터만 선택해서 새로운 데이터프레임 생성

mask_value_counts = mask.value_counts()
print(f"mask.count = {mask.count()}")
print(f"mask._value_counts() = {mask.value_counts()}")
print(f"df_seoul.count() = {df_seoul.count()}")

# 전출지가 어차피 서울이니까 삭제
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
# 전입지별 이름을 전입지로 바꿈
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# 전입지를 인덱스로 설정
df_seoul.set_index('전입지', inplace=True)

# iloc, loc를 이용해 서울에서 경기도로 이동한 인구 데이터 값만 선택 
sr_one = df_seoul.loc['경기도']

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values)

# 제목 축이름 없이 바로 그래프 만들수 있음
# plt.plot(sr_one)

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동')

# 축이름 추가
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 판다스 객체를 plot 함수에 입력
plt.show()


#%%
# 제목추가

plt.title('서울 -> 경기 인구 이동')  #차트 제목
plt.xlabel('기간')                  #x축 이름
plt.ylabel('이동 인구수')           #y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best')     #범례 표시

#%% 

# 스타일 서식 지정
plt.style.use('ggplot') 

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력 
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 표시 추가