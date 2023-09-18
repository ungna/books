#!/usr/bin/env python
# coding: utf-8

# # 01-3 이 도서가 얼마나 인기가 좋을까요?

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 도서 데이터 찾기

# [공공데이터포털](https://www.data.go.kr/)
# 
# 도서관 정보나루의 [남산도서관 장서/대출 목록](https://www.data4library.kr/openDataV?libcode=4707)

# ## 코랩에서 데이터 확인하기

# In[1]:


import gdown

gdown.download('https://bit.ly/3eecMKZ', 
               '남산도서관 장서 대출목록 (2021년 04월).csv', quiet=False)


# ## 파이썬으로 CSV 파일 출력하기

# In[ ]:


with open('남산도서관 장서 대출목록 (2021년 04월).csv', encoding = "euc-kr") as f:
    print(f.readline())


# In[16]:


fp = open('남산도서관 장서 대출목록 (2021년 04월).csv')
for rd in fp.readline():
    print(rd)
fp.close()


# In[3]:


import chardet

with open('남산도서관 장서 대출목록 (2021년 04월).csv', mode='rb') as f:
    d = f.readline()

print(chardet.detect(d))


# In[4]:


with open('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr') as f:
    print(f.readline())
    print(f.readline())


# In[5]:

import os
import glob
import unicodedata

# MacOs: NFD
# Windows, Linux: NFC  
for filename in glob.glob('*.csv'):
  nfc_filename = unicodedata.normalize('NFC', filename)
  os.rename(filename, nfc_filename)


# ## 데이터프레임 다루기: 판다스

# In[6]:


import pandas as pd


# In[7]:


# df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr')


# In[9]:


# low_memory옵션은 대용량의 데이터를 불러오는 경우 각 칼럼의 데이터 타입(dtype)을 추측하는 것이 
# 매우 많은 메모리를 사용하기 때문에 대용량의 데이터를 불러올때 메모리 에러가 발생하는 경우 
# 이를 False로 설정할 것을 권장한다.
df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 low_memory=False)
df.head()


# In[11]:


df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 dtype={'ISBN': str, '세트 ISBN': str, '주제분류번호': str})
df.head()


# In[12]:


df.to_csv('ns_202104.csv')


# In[13]:

# encoding="utf-8"을 안넣어서 버그남
# notepadd++로 열어서 인코딩 확인
"""
with open('ns_202104.csv', encoding="utf-8") as f:
    for i in range(3):  # 위에서 3 라인만 읽어옴
        print(f.readline(), end='')
"""

# In[14]:

# ns_202104.csv로 바꿈
ns_df = pd.read_csv('ns_202104.csv', low_memory=False)
ns_df.head()


# In[15]:

# ns_202104.csv로 바꾸면서 index_col=0 
# 자꾸Unnamed=0 이라는 칼럼이 뜨는데 이거 없애줌
ns_df = pd.read_csv('ns_202104.csv', index_col=0, low_memory=False)
ns_df.head()


# In[ ]:


df.to_csv('ns_202104.csv', index=False)


# In[ ]:


# 코랩을 사용하는 경우 xlsxwriter 패키지를 설치해 주세요.
# get_ipython().system('pip install xlsxwriter')


# In[ ]:


ns_df.to_excel('ns_202104.xlsx', index=False, engine='xlsxwriter')

print("엑셀파일 생성종료")  # 오래걸리니까 완료됬는지 확인용

