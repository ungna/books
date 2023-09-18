
import pandas as pd

card = pd.read_excel('악추피계산기.xlsx', engine='openpyxl', 
                    header=None)  # header=None 옵션

card.head()
print(card.columns)

card.columns = ["빈칸", "등급", "이름", "각성", "여유", "머야이거"]

print(card.columns)


# 필요없는거 지우기
card = card.drop("빈칸", axis=1)
card = card.drop("각성", axis=1)
card = card.drop("여유", axis=1)
card = card.drop("머야이거", axis=1)

#%%
# 이름, 등급으로 되있는거 nan으로 바꾸기
# 특정 행을 찾아서 지우기 힘드니까 nan으로 바꾸고 nan전부 지우게
import numpy as np
card['이름'].replace('이름', np.nan, inplace=True)

#%%
# nan만있는행 지우기 
# 이름이 nan인걸 기준으로 지움
card.dropna(subset = ["이름"], how='any', axis=0, inplace = True)

#%%
# 셀병합한거 합치기
card.ffill(inplace = True)

#%%
# 카드 등급 머있는지 확인
print(card["등급"].unique())


