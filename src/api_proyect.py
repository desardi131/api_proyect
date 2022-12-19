from flask import Flask, render_template, request
from acceso import acceso
from predict import pred_to_csv, grafica_pred
import error as e

import pickle
import numpy as np
import pandas as pd
import pymysql
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

# Esto es sólo pa subir los últimos 30 días de la base de datos
@app.route('/actualizar', methods=['POST'])
def actualizar():
    return render_template('actualizar.html', tables = [acceso('mes').to_html()], titles=[''])

@app.route('/predict')
def predict():
    e.mape()
    return render_template('predict.html')

@app.route('/after_predict', methods=['POST'])
def after_predict():
    pred_to_csv(request.form['day'])
    grafica_pred()
    return render_template('after_predict.html')

@app.route('/health/', methods=['GET'])
def health():
    return "everything os here"

if __name__ == "__main__":
    app.run(debug=True)