#!/usr/bin/env python
# coding: utf-8

# # 04-1 통계로 요약하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 기술통계 구하기

# In[1]:


import gdown

gdown.download('https://bit.ly/3736JW1', 'ns_book6.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book6 = pd.read_csv('ns_book6.csv', low_memory=False)
ns_book6.head()


# In[3]:


ns_book6.describe()


# In[4]:


sum(ns_book6['도서권수']==0)


# In[5]:


ns_book7 = ns_book6[ns_book6['도서권수']>0]


# In[6]:


ns_book7.describe(percentiles=[0.3, 0.6, 0.9])


# In[7]:


ns_book7.describe(include='object')


# ## 평균

# $평균 = \dfrac{a + b + c}{3}$
# 
# $평균 = \dfrac{x_1 + x_2 + x_3}{3}$

# In[8]:


x = [10, 20, 30]
sum = 0
for i in range(3):
    sum += x[i]
print("평균:", sum / len(x))


# $평균 = \dfrac{x_1 + x_2 + x_3}{3} = \dfrac{\sum_{i=1}^{3} x_i}{3}$
# 
# $평균 대출건수 = \dfrac{\sum_{i=1}^{376770} x_i}{376770}$

# In[9]:


ns_book7['대출건수'].mean()


# ## 중앙값

# In[10]:


ns_book7['대출건수'].median()


# In[11]:


temp_df = pd.DataFrame([1,2,3,4])
temp_df.median()


# In[12]:


ns_book7['대출건수'].drop_duplicates().median()


# ## 최솟값, 최댓값

# In[13]:


ns_book7['대출건수'].min()


# In[14]:


ns_book7['대출건수'].max()


# ## 분위수

# In[15]:


ns_book7['대출건수'].quantile(0.25)


# In[16]:


ns_book7['대출건수'].quantile([0.25,0.5,0.75])


# In[17]:


pd.Series([1,2,3,4,5]).quantile(0.9)


# In[18]:


4 + (0.9-0.75)*(5-4)/(1.0-0.75)


# In[19]:


pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='midpoint')


# In[20]:


pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='nearest')


# In[21]:


borrow_10_flag = ns_book7['대출건수'] < 10


# In[22]:


borrow_10_flag.mean()


# In[23]:


ns_book7['대출건수'].quantile(0.65)


# ## 분산

# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}$
# 
# $ \bar{x} = \dfrac{\sum_{i=1}^n x_i}{n}$

# In[24]:


ns_book7['대출건수'].var()


# ## 표준 편차

# $ s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}}$

# In[25]:


ns_book7['대출건수'].std()


# $\sqrt{4}=2$

# In[26]:


import numpy as np

diff = ns_book7['대출건수'] - ns_book7['대출건수'].mean()

np.sqrt( np.sum(diff**2) / (len(ns_book7)-1) )


# ## 최빈값

# In[27]:


ns_book7['도서명'].mode()


# In[28]:


ns_book7['발행년도'].mode()


# ## 데이터프레임에서 기술통계 구하기

# In[29]:


ns_book7.mean(numeric_only=True)


# In[30]:


ns_book7.loc[:, '도서명':].mode()


# In[31]:


ns_book7.to_csv('ns_book7.csv', index=False)


# ## 넘파이의 기술통계 함수

# ### 평균 구하기

# In[32]:


import numpy as np

np.mean(ns_book7['대출건수'])


# $\dfrac{국어점수 \times 2 + 수학점수}{3}$
# 
# $\dfrac{국어점수 \times 국어가중치 + 수학점수 \times 수학가중치}{국어가중치 + 수학가중치}$ 
# 
# $가중평균 = \dfrac{x_1 \times w_1 + x_2 \times w_2}{w_1 + w_2} = \dfrac{\sum_{i=1}^{2} x_i \times w_i}{\sum_{i=1}^{2} w_i}$

# In[33]:


np.average(ns_book7['대출건수'], weights=1/ns_book7['도서권수'])


# In[34]:


np.mean(ns_book7['대출건수']/ns_book7['도서권수'])


# In[35]:


ns_book7['대출건수'].sum()/ns_book7['도서권수'].sum()


# ### 중앙값 구하기

# In[36]:


np.median(ns_book7['대출건수'])


# ### 최솟값, 최댓값 구하기

# In[37]:


np.min(ns_book7['대출건수'])


# In[38]:


np.max(ns_book7['대출건수'])


# ### 분위수 구하기

# In[39]:


# interpolation 매개변수가 numpy 1.22(python >= 3.8) 버전부터 method로 바뀜
np.quantile(ns_book7['대출건수'], [0.25,0.5,0.75])


# ### 분산 구하기

# In[40]:


np.var(ns_book7['대출건수'])


# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$

# In[41]:


ns_book7['대출건수'].var(ddof=0)


# In[42]:


np.var(ns_book7['대출건수'], ddof=1)


# ### 표준 편차 구하기

# In[43]:


np.std(ns_book7['대출건수'])


# ### 최빈값 구하기

# In[44]:


values, counts = np.unique(ns_book7['도서명'], return_counts=True)
max_idx = np.argmax(counts)
values[max_idx]


# ## 확인문제

# #### 4.

# In[45]:


ns_book7[['출판사','대출건수']].groupby('출판사').mean().sort_values('대출건수', ascending=False).head(10)


# #### 5.

# In[46]:


target_range = np.array(ns_book7['대출건수'].quantile(q=[0.25,0.75]))
target_bool_idx = (ns_book7['대출건수'] >= target_range[0]) & (ns_book7['대출건수'] <= target_range[1])
target_bool_idx.sum()/len(ns_book7)*100

