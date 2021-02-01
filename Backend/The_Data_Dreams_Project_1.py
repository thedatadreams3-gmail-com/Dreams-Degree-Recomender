#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('Courses_data.csv')


# # Pre-Processing & Cleaning
# 

# In[3]:


cleaned_data = df.copy()

#cleaned_data.drop('Courses', axis=1, inplace=True)


# ## Replace Name

# In[4]:


degree_unique = cleaned_data['Study Program'].unique()

print(degree_unique)


# In[5]:



rem = [0,2,4,6,7,10,12,14,15,16,20,22,23,24,25,26,27,28,29,38,40,42,45]
replace_name = degree_unique[rem]
tobe_replaced = cleaned_data[cleaned_data['Study Program'].isin(replace_name)] 

wanted = cleaned_data[~cleaned_data['Study Program'].isin(replace_name)] 
wanted_name= wanted['Study Program'].unique()

wanted_name= np.delete(wanted_name,[22])

count=0
for i in replace_name:
    cleaned_data['Study Program'].replace(to_replace=i, value=wanted_name[count], inplace=True)
    count+=1


# In[6]:


cleaned_data['Study Program'].unique()


# In[7]:


cleaned_data.to_csv('cleaned_data.csv')


# ## Text Cleaning

# In[40]:


import re
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import dill
import pickle
import marshal




def prep_desc(a : str):
    ''' clean description to be more managable '''
    # take out special characters
    a = re.sub('[^A-Za-z0-9]+', ' ', a)
    # take out single characters
    a = re.sub(r'\s+[a-zA-Z]\s+', ' ', a)
    # take out single characters from start
    a = re.sub(r'\^[a-zA-Z]\s+', ' ', a)
    # take out double spaces
    a = re.sub(r'\s+', ' ', a, flags=re.I)
    # change all to lower case
    a = a.lower()
    # tokenize
    words = word_tokenize(a)
    # remove punctuation
    words_no_punc= []
    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())
    # remove stopwords
    clean_words = []
    for w in words_no_punc:
        if w not in stopwords.words("english"):
            clean_words.append(w)
    
    
    a = ' '.join(clean_words)
    
    return a

code_string = marshal.dumps(prep_desc.func_code)
pickle.dump(code_string, open("cleaning.pkl", "wb"))

    


# In[9]:


cleaned_data.iloc[55]['Description']


# In[10]:


cleaned_data['Description']=cleaned_data['Description'].apply(prep_desc)


# In[11]:


cleaned_data.iloc[55]['Description']


# In[12]:


cleaned_data.head()


# In[13]:


cleaned_data.to_csv('cleaned_data.csv')


# # Document-Term Matrix

# ## Group cleaned data by Degree

# In[14]:


cleaned_data_grouped = cleaned_data.copy()


# In[15]:


cleaned_data_grouped = cleaned_data_grouped.groupby(cleaned_data_grouped['Study Program'])['Description'].apply(lambda x: ' '.join(x)).reset_index()
cleaned_data_grouped.index = cleaned_data_grouped['Study Program']
cleaned_data_grouped.drop(columns=['Study Program'], inplace =True)
cleaned_data_grouped.head()


# In[16]:


cleaned_data_grouped.info()


# ## Creating DTM using CountVectorizer

# In[17]:


from sklearn.feature_extraction.text import CountVectorizer


cv = CountVectorizer()
data_cv = cv.fit_transform(cleaned_data_grouped['Description'])

dtm = pd.DataFrame(data_cv.toarray(), columns = cv.get_feature_names())
dtm.index = cleaned_data_grouped.index
dtm


# # Data Analysis

# ## Count how many description available for each degree

# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize':(11.7,8.27)})

sns.countplot(x='Study Program', data=cleaned_data)


# ## Most Common Words for each degree

# ### Finding Common Words

# In[19]:


# transpose dtm

dtmT = dtm.transpose()
dtmT


# In[20]:


# using Tansposed dtm
top_dict = {}
for c in dtmT.columns:
    top = dtmT[c].sort_values(ascending=False).head(50)
    top_dict[c] = list(zip(top.index, top.values))
    
    
top_dict


# In[21]:


for degree, top_words in top_dict.items():
    print(degree)
    print(', '.join([word for word, count in top_words[0:29]]))
    print('---')


# ## Creating WordCloud

# In[22]:


from wordcloud import WordCloud

wc = WordCloud(background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)

plt.rcParams['figure.figsize'] = [30,10]

degrees = cleaned_data['Study Program'].unique()

for index, degree in enumerate(dtmT.columns):
    wc.generate(cleaned_data_grouped.Description[degree])
    
    plt.subplot(5 ,5,index +1)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(degrees[index])
    
    
plt.show()


# using Transposed dtm


# In[23]:


cleaned_data_grouped.Description['B.Sc. Industrial Engineering (Mechanical Engineering and Management)  PO19 - B-WI(MB)-19']


# ### TODO get words that is not needed to extend for stopwords

# # Training

# ## features extraction using tf-idf

# In[24]:


from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer(analyzer = 'word')
X = vectorizer.fit_transform(cleaned_data['Description'])
Y = cleaned_data['Study Program']
feat = vectorizer.get_feature_names()


# In[25]:


'''
for i in range(len(cleaned_data['Description'])):
    for j in range(len(feat)):
        if X[i,j]!=0.0:
            print(i , feat[j], X[i,j])
            
'''


# In[26]:


print(len(cleaned_data['Description']))


# ## Recommend using rfc

# In[27]:


from sklearn.ensemble import RandomForestClassifier

text_classifier_rfc = RandomForestClassifier(n_estimators=100, random_state=0)  
text_classifier_rfc.fit(X, Y)


# In[28]:


W = str('Graduates with a Master degree in Electrical Engineering, Information Technology, and Computer Engineering with a specialization in Computer Engineering will have acquired a high level of specialization, a research-oriented view, and in-depth, domain-specific knowledge at a professional level in the areas of computer technology, information/communication technology, and/or media technology. They will be able to understand how the different components of a complex system are connected and functionally combined, and they will be able to apply theoretical concepts of system identification, modelling, and optimization in order to further develop such systems on their own, particularly by hardware/software co-design. Examples of such systems include general computer systems, media systems (image/video/speech/audio processing, recognition, and coding), automated and embedded systems, robotics, automotive systems, and many more. In the given field, the graduates will be able')
#W= str('i like math coding programming and logic')
#W = str('course conveys phenomena theories neurobiological foundations well fundamental current studies regarding following topics psychology empirical science foundations neuroanatomy perception attention behavior motor skills executive functions learning memory thinking problem solving decision making')


# In[29]:


W=prep_desc(W)
print(W)


# In[30]:


W = vectorizer.transform([prep_desc(W)])
prediction = text_classifier_rfc.predict(W)
print(prediction)


# ## Recommend using SVM

# In[31]:


from sklearn import svm

text_classifier_svm = svm.SVC(kernel='linear')
text_classifier_svm.fit(X, Y)


# In[32]:


prediction = text_classifier_rfc.predict(W)
print(prediction)


# ## Recommend using Cos Sim

# In[33]:


cleaned_data.iloc[0]['Description']


# In[34]:


from sklearn.metrics.pairwise import cosine_similarity



cosine_sim = cosine_similarity(X, W)


# In[35]:


print(cosine_sim)


# In[36]:


import heapq

top_ten = heapq.nlargest(10 , cosine_sim)
print(top_ten)


# In[37]:


print(cosine_sim[1])


# In[38]:



for i in range(len(cosine_sim)):
    for j in top_ten:
        if cosine_sim[i]==j:
            print(cleaned_data.iloc[i]['Study Program'] , j)


# In[ ]:




