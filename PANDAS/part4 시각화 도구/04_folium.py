# leaflet.js 기반으로 만들어진 Python 지도 시각화 라이브러리
import folium 

# 서울지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)

# 지도를 HTML형태로 만들기
seoul_map.save('./data_made/seoul.html')

#%%
# map tiles로 다른 스타일의 지도 만들기
# 서울 지도 만들기
seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', 
                        zoom_start=15)

# 지도를 HTML 파일로 저장하기
seoul_map2.save('./data_made/seoul2.html')
seoul_map3.save('./data_made/seoul3.html')

#%%
# marker
# 라이브러리 불러오기
import pandas as pd
import folium

# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('./서울지역 대학교 위치.xlsx', engine= 'openpyxl')

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

df.rename(columns={'Unnamed: 0': '대학이름'}, inplace=True)

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.대학이름, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('./data_made/seoul_colleges.html')

#%%
print(f"index: {df.index}")
print(f"위도: {df.위도}")
print(f"경도: {df.경도}")    
print(df.columns[0])
#%%
# 학원위치(37.29171, 127.01241) marker해보기

# 라이브러리 불러오기
import pandas as pd
import folium

# 학원위치 설정
lat = 37.29171
lng = 127.01241
name = 'YSIT아카데미'

# 지도 만들기 
ys_map = folium.Map(location=[37.29 ,127.01], zoom_start=16)

# 원하는 위치에 marker표시
folium.Marker([lat, lng], popup=name).add_to(ys_map)

# HTML로 저장
ys_map.save('./data_made/YSIT.html')