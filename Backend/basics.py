from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re
import pickle
import marshal,types
import dill
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer#
import nltk
import re
import pandas as pd

model = pickle.load(open('svmDegreePredictor.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
kmeans = pickle.load(open('clusterRecommender.pkl', 'rb'))
clusterVectorizer = pickle.load(open('clusterVectorizer.pkl', 'rb'))
dfCluster = pickle.load(open('dfCluster.pkl', 'rb'))
gensimDf = pickle.load(open('gensimDf.pkl', 'rb'))
gensimModel = pickle.load(open('gensimModel.pkl', 'rb'))
gensimDegreeDf = pickle.load(open('gensimDegreeDf.pkl', 'rb'))
gensimDegreeModel = pickle.load(open('gensimDegreeModel.pkl', 'rb'))
cleaner_code=pickle.load(open('cleaning.pkl', 'rb'))
all_courses_tfidf=pickle.load(open('all_courses_tfidf.pkl', 'rb'))
SP_Course_Tuple=pickle.load(open('SP_Course_Tuple.pkl', 'rb'))
#furkanFunction =pickle.load(open('furkanFunctions.pkl', 'rb'))

 #Input for Recommendation
text = "I like designing and organizing projects. I enjoy doing art, and to visualize solutions."
stop = list(stopwords.words('english'))
stop.extend('systems system develop developed development method methods lecture basic function functions course fundamental problem basic basics first topic concept concepts convey conveys exercise exercises content contents including student students well part introduction main aim pre used one pre existing contains deals introduced new really like'.split())
#further extended stop words: main aim pre used one pre existing contains deals introduced new really like think interested
#problem: words like physics, chemistry have no matches 
#problem2: mostly applied cognitive and media science recommended
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
        if w not in stop:
            clean_words.append(w)
    #stem_words=[stemmer.stem(w) for w in clean_words]
    #lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    #lemma_words=[lemmatizer.lemmatize(w) for w in clean_words]
    a = ' '.join(clean_words)
    #a = ' '.join(stem_words)
    return a

#furkan's function
def getCoursesTfidf(all_courses_tfidf,keywords_list):
    all_course_keywords_tfidf=[]
    for cw in all_courses_tfidf:
        match_course_keywords = []
        for w in cw[1]: 
            #leave out empty strings and multiple occurences of a keyword in a course (cause its tfidf already is taken into account)
            if w[1] in keywords_list and w[1] != None and w[1] not in [k[1] for k in match_course_keywords]:
                match_course_keywords.append((w[0], w[1]))
        all_course_keywords_tfidf.append((cw[0], match_course_keywords))
    return all_course_keywords_tfidf

def getCoursesTfidfSumUps(all_course_keywords_tfidf):
    course_results=[]
    for cmk in all_course_keywords_tfidf:
        result = 0
        for mk in cmk[1]:
            result = result + mk[0]
        course_results.append((result, cmk[0]))
    return course_results
        
def getFinalCourseResults(course_results):
    final_course_results=[]
    for x in course_results:
        if x[0]>0:
            final_course_results.append(x)
    return sorted(final_course_results)

def getAllcoursesKeywordsTfidf(all_course_keywords_tfidf):
    course_keywords = []
    for c in all_course_keywords_tfidf:
        for ck in c[1]:
            if ck[1] not in course_keywords:
                course_keywords.append(ck[1])
    return course_keywords

def maxTfidf(course_keywords, all_course_keywords_tfidf):
    max_k_tfidfs=[]
    for k in course_keywords:
        max_k_value = 0
        for c in all_course_keywords_tfidf:
            for ck in c[1]:
                if k == ck[1]:
                    if max_k_value < ck[0]:
                        max_k_value = ck[0]
        max_k_tfidfs.append((k, max_k_value))
    return max_k_tfidfs

def getCoursePercentages(final_course_results):
    final_course_percentages=[]
    max_sum_tfidf=[]
    for fcr in final_course_results:
        percentage = 0.0
        percentage = (fcr[0] / max_sum_tfidf) * 100
        final_course_percentages.append((percentage, fcr[1]))
    return final_course_percentages

def getSpAndCoursesAndTfidfResults(SP_Course_Tuple, final_course_results):
    SP_course_results=[]
    for t in SP_Course_Tuple:
        match_courses = []
        for r in final_course_results:
            if r[1] in t[1]:
                match_courses.append(r)
        SP_course_results.append((t[0], match_courses))
    return SP_course_results

def getFinalStudyProgramSumUps(SP_course_results):
    final_SP_results=[]
    for s in SP_course_results:
        f_result = 0
        for r in s[1]:
            f_result = f_result + r[0]
        if f_result != 0:
            final_SP_results.append((f_result, s[0]))
    return sorted(final_SP_results)





app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def home():
    #Cleaning Data
    data1= request.get_json()['a']
    data1=prep_desc(data1)
    #print(data1)

    #furkan code
    keywords = data1
    keywords_list = keywords.split()
    #print (keywords_list)
    #print('keywords:', keywords_list)
    #get all matching keywords from all collected keywords with tfidf value
    all_course_keywords_tfidf = getCoursesTfidf(all_courses_tfidf,keywords_list)
    #print(all_course_keywords_tfidf)

    #get each course + tidf_results(summed up) 
    course_results = []
    course_results = getCoursesTfidfSumUps(all_course_keywords_tfidf)

    #get all courses with results > 0
    final_course_results = []
    final_course_results = getFinalCourseResults(course_results)



    
    course_keywords = getAllcoursesKeywordsTfidf(all_course_keywords_tfidf)

    #get the highest tfidfs from all courses
    max_k_tfidfs = []
    max_k_tfidfs = maxTfidf(course_keywords, all_course_keywords_tfidf)

    #print(max_k_tfidfs)

    #sum up all max tfidf to get highest value a course can have 
    max_sum_tfidf = sum(v[1] for v in max_k_tfidfs)
    #print(max_sum_tfidf)

    #get 'similarity' for each course regarding how much it matches the hundred percent
    #final_course_percentages = []
    #final_course_percentages = getCoursePercentages(final_course_results, max_sum_tfidf)

    #assign each course (+ result) to its Study Programs
    SP_course_results = []
    SP_course_results = getSpAndCoursesAndTfidfResults(SP_Course_Tuple, final_course_results)

    #for s in SP_course_results:
    #print(s)
    
    #final results: sum up all course results to get final results for each study program 
    final_SP_results = []
    final_SP_results = getFinalStudyProgramSumUps(SP_course_results)
        
    
    
    
    
    #SVM Prediction and Clustering 
    
    Y= vectorizer.transform([data1])
    W= clusterVectorizer.transform([data1])
    prediction = model.predict(Y)
    cluster=kmeans.predict(W)
    #print(prediction)
    #print(type(dfCluster['Study Program'][3]))
    prediction=''.join(map(str, prediction))
    #print(prediction)

    

   
    # prediction=prediction.tostring()
    #print(type(prediction))
    cl=0
    clusterList=[]
    #prediction=re.sub('[', '', prediction)
    #prediction=re.sub(']', '', prediction)

    for index, row in dfCluster.iterrows():
       if(prediction in row['Study Program']):
           cl=row['Cluster']
           break

    for index, row in dfCluster.iterrows():
        if (row['Cluster'] == cl) :
           clusterList.append(row['Study Program'])


    #print(cl)

     #Gensim Course Model Prediction
    new_vec=gensimModel.infer_vector(data1.split())
    similar_doc = gensimModel.docvecs.most_similar([new_vec])
    gensimlst=[]
    #for row,index in similar_doc:
        #print(gensimDf['Study Program'][row]+ ' - '+ gensimDf['Courses'][row] + ' - Similarity= ' + str(index))
     #   gensimlst.append(gensimDf['Study Program'][row]+ ' - '+ gensimDf['Courses'][row] + ' - Similarity= ' + str(index))

    #removing duplicates
    pred = []
    for row,index in similar_doc:
        pred.append(
            {
                'Study Program':gensimDf['Study Program'][row] ,
                'Courses': gensimDf['Courses'][row],
                'Similarity':  str(index)
            }
        )

    pred=pd.DataFrame(pred)
    pred.drop_duplicates(inplace=True, subset=['Study Program','Courses'])

    #converting back to lists
    for index, row in pred.iterrows():
        gensimlst.append({
            'studyProgram': row['Study Program'],
            'courses': row['Courses'],
            'similarity': row['Similarity']
        })

    #Gensim Degree Model Prediction
    new_Degree=gensimDegreeModel.infer_vector(data1.split())
    similar_degree= gensimDegreeModel.docvecs.most_similar([new_Degree])
    gensimDegree=[]
    for row,index in similar_degree:
        #print(gensimDegreeDf['Study Program'][row] + ' - Similarity= ' + str(index))
        gensimDegree.append({
            'program': gensimDegreeDf['Study Program'][row],
            'similarity': index
        })


    return jsonify({
        'prediction': prediction,
        'clusterList': clusterList,
        'gensimList': gensimDegree,
        'furkansList': final_SP_results[-10:],
        'gensimCourse': gensimlst
        })
    




if __name__ == "__main__":
    app.run(debug=True)


