import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vect = CountVectorizer(vocabulary=pickle.load(open("feature.pkl", "rb")))
tfidf = pickle.load(open("tfidf.pkl", 'rb'))
enc = pickle.load(open("enc.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # read the data
    features = np.array([str(x) for x in request.form.values()])
    
    #preprocess data and predict
    output = preprocess_predict(features)

    return render_template('index.html', prediction_text=f'Job Industry is:  {output}');

@app.route('/predict_api/<string:job>',methods=['GET'])
def predict_api(job):
    '''
    For rendering results as json and get input directly from url 
    '''
    #get data
    features = np.array([job])
    
    #preprocess data and predict
    output = preprocess_predict(features)
    
    return jsonify({"Job Industry": output})
    
    
def preprocess_predict(data):

    #preprocess data
    features = vect.transform(data).toarray()
    features = tfidf.transform(features).toarray()
    
    #predict
    industry_code = model.predict(features)
    industry_name = enc.inverse_transform(industry_code.reshape(-1,1))[0][0]
    
    #output
    return industry_name
    

if __name__ == "__main__":
    app.run(debug=True)