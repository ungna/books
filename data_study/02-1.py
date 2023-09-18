#!/usr/bin/env python
# coding: utf-8

# # 02-1 API 사용하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 파이썬에서 JSON 데이터 다루기

# In[1]:


d = {"name": "혼자 공부하는 데이터 분석"}

print(d['name'])   # class 'dict'


# In[2]:


import json


# In[3]:

# json.dumps  Python의 객체를 JSON 문자열로 변환
d_str = json.dumps(d, ensure_ascii=False)
print(d_str)


# In[4]:


print(type(d_str))


# In[5]:


# json.loads  JSON 문자열을 Python의 객체로 변환
d2 = json.loads(d_str)

print(d2['name'])


# In[6]:


print(type(d2))   # class 'dict'


# In[7]:


d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022}')

# dict key로 value읽기
print(d3['name'])
print(d3['author'])
print(d3['year'])


# In[8]:


d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": ["박해선","홍길동"], \
                  "year": 2022}')

print(d3['author'][1])   # 박해선


# In[9]:


d4_str = """
[
  {"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name": "혼자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""
d4 = json.loads(d4_str)

print(d4[0]['name'])   # 혼자 공부하는 데이터 분석


# In[10]:


import pandas as pd

pd.read_json(d4_str)


# In[11]:

pd.DataFrame(d4)



# In[12]:

# 파이썬에서 XML 다루기

x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""


# In[13]:


import xml.etree.ElementTree as et
# xml.etree.ElementTree : XML을 다룰때 많이 사용됨
# https://pythonblog.co.kr/coding/15/

book = et.fromstring(x_str)


# In[14]:


print(type(book))   # <class 'xml.etree.ElementTree.Element'>


# In[15]:


print(book.tag)     # book


# In[16]:


book_childs = list(book)
# book 안에 들어있는 Element들을 리스트로 가지고 온거임

print(book_childs)
"""
[<Element 'name' at 0x0000023414C12840>, 
 <Element 'author' at 0x0000023414C13830>, 
 <Element 'year' at 0x0000023414C12B10>]

"""
# In[17]:

# Element를 객체에 넣음
name, author, year = book_childs

print(name.text)
print(author.text)
print(year.text)

# <tag> text </tag>  # 즉 name태그 안에있는 문자


# In[18]:

# findtext('tag')로 <tag>안에있는 텍스트를 가지고옴
name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')

print(name)
print(author)
print(year)


# In[19]:


x2_str = """
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼자 공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""


# In[20]:


books = et.fromstring(x2_str)

print(books.tag)    # books
# 제일 상위에 있는 tag를 가지고옴


# In[21]:


for book in books.findall('book'):  # <book>의 내용물을 전부 찾음  반복문으로 2개다 찾음
    name = book.findtext('name')    # <name></name> 안의 텍스트를 가지고옴
    author = book.findtext('author')
    year = book.findtext('year')
    
    print(name)
    print(author)
    print(year)
    print()


# In[22]:

# 차이점 한번보기
pd.read_xml(x2_str)
print(x2_str)

# ## 파이썬으로 API 호출하기

# In[23]:


import requests


# In[24]:

url = "http://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"


# In[25]:

# method= get 방식으로 ? 뒤에서 정보를 넣음
"""
http://data4library.kr/api/loanItemSrch?

format=json&
startDt=2021-04-01&
endDt=2021-04-30&age=20&
authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2
"""
r = requests.get(url)


# In[26]:


data = r.json()

print(data)


# In[27]:


data


# In[28]:


data['response']['docs']


# In[29]:


books = []
for d in data['response']['docs']:
    books.append(d['doc'])


# In[30]:


books = [d['doc'] for d in data['response']['docs']]


# In[31]:


books


# In[32]:


books_df = pd.DataFrame(books)

books_df


# In[33]:


books_df.to_json('20s_best_book.json')

