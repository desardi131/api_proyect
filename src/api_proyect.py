from flask import Flask, render_template, request,redirect, url_for, flash, jsonify
import pickle
import numpy as np

# model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__) 



@app.route('/')
def man():
    return render_template('home_app.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/re_train')
def re_train():
    return render_template('re_train.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/after_predict', methods=['POST'])
def after_predict():
    return render_template('after_predict.html')


if __name__ == "__main__":
    app.run(debug=True) 