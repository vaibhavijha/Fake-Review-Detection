
from flask import Flask, jsonify, request
import joblib, string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from flask_pymongo import pymongo

app = Flask(__name__)

# ============================== TEXT PROCESSING ===================================
def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    tmp = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return tmp

# ============================== LOAD SAVED MODEL ===================================
model = joblib.load('model.pkl')


# ============================== API TO PREDICT THE REVIEW IS FAKE OR NOT ===========
@app.route('/predict', methods=['POST'])
def predict():
    # get the input data from the request
    data = request.get_json()
    review = data['review']
    list_review = [review]
    predictions = model.predict(list_review)
    isFake = False
    if predictions[0] == "CG":
        isFake = True
    return jsonify({'isFake': isFake})


 # ============================== SIGNIN ===================================
# driver function
if __name__ == '__main__':

	app.run(debug = True)
