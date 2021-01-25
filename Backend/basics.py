from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re
import pickle

model = pickle.load(open('svmDegreePredictor.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
kmeans = pickle.load(open('clusterRecommender.pkl', 'rb'))
clusterVectorizer = pickle.load(open('clusterVectorizer.pkl', 'rb'))
dfCluster = pickle.load(open('dfCluster.pkl', 'rb'))
gensimDf = pickle.load(open('gensimDf.pkl', 'rb'))
gensimModel = pickle.load(open('gensimModel.pkl', 'rb'))




app = Flask(__name__)
CORS(app)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    #SVM Prediction and Clustering 
    data1 = request.get_json()['a']
    Y= vectorizer.transform([data1])
    W= clusterVectorizer.transform([data1])
    prediction = model.predict(Y)
    cluster=kmeans.predict(W)
    print(prediction)
    print(type(dfCluster['Study Program'][3]))
    prediction=''.join(map(str, prediction))
    print(prediction)

    

   
    # prediction=prediction.tostring()
    print(type(prediction))
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


    print(cl)

     #Gensim Model Prediction
    new_vec=gensimModel.infer_vector(data1.split())
    similar_doc = gensimModel.docvecs.most_similar([new_vec])
    gensimlst=[]
    for row,index in similar_doc:
        # print(gensimDf['Study Program'][row]+ ' - '+ gensimDf['Courses'][row] + ' - Similarity= ' + str(index))
        # gensimlst.append(gensimDf['Study Program'][row]+ ' - '+ gensimDf['Courses'][row] + ' - Similarity= ' + str(index))
        gensimlst.append({
            'program': gensimDf['Study Program'][row],
            'similarity': index
        })



    print("------", prediction, "------", clusterList, "------", gensimlst)
    return jsonify({
        'prediction': prediction,
        'clusterList': clusterList,
        'gensimList': gensimlst
    })
    # return render_template('prediction.html', pred=prediction, cl=cl, clusterList=clusterList, gensimlst=gensimlst)
    




if __name__ == "__main__":
    app.run(debug=True)


