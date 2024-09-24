from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    polarity=sentimentCal(text)
    return render_template('result.html', text=text, polarity=polarity)
    
    
@app.get('/postman')
def postman():
    data = request.get_json()
    text = data['text']
    polarity =sentimentCal(text)
    return jsonify({
        'polarity': polarity
    })
    
def sentimentCal(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity
