from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import pickle

model = pickle.load(open('svmDegreePredictor.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
kmeans = pickle.load(open('clusterRecommender.pkl', 'rb'))
clusterVectorizer = pickle.load(open('clusterVectorizer.pkl', 'rb'))


app = Flask(__name__)
CORS(app)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.get_json()['a']
    Y= vectorizer.transform([data1])
    W= clusterVectorizer.transform([data1])
    prediction = model.predict(Y)
    cluster=kmeans.predict(W)
    print(prediction)
    return jsonify({
        'prediction': str(prediction[0]),
        'cluster': int(cluster[0])
    })
    




if __name__ == "__main__":
    app.run(debug=True)


