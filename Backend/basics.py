from flask import Flask, render_template, request

import pickle

model = pickle.load(open('svmDegreePredictor.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
kmeans = pickle.load(open('clusterRecommender.pkl', 'rb'))
clusterVectorizer = pickle.load(open('clusterVectorizer.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1= request.form['a']
    Y= vectorizer.transform([data1])
    W= clusterVectorizer.transform([data1])
    prediction = model.predict(Y)
    cluster=kmeans.predict(W)
    print(prediction)
    return render_template('prediction.html', pred=prediction, clus=cluster)
    




if __name__ == "__main__":
    app.run(debug=True)


