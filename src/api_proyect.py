from flask import Flask, render_template
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
@app.route('/update', methods=["GET"])
def get_all():
    username = "DataScienceTB22"
    password = "pyquirrinds"
    host = "database-1.ceaq9kvyuwau.us-east-2.rds.amazonaws.com"
    port = "3306"
    cursorclass = pymysql.cursors.DictCursor

    # gets the credentials from .aws/credentials 
    db = pymysql.connect(host=host,
                         user=username,
                         password=password,
                         cursorclass=cursorclass,
                         )

    cursor = db.cursor()

    cursor.connection.commit()
    use_db = ''' USE users_web'''
    cursor.execute(use_db)

    sql = '''SELECT * FROM users'''
    cursor.execute(sql)
    tabla = cursor.fetchall()
    tabla = pd.DataFrame(tabla)
    tabla = tabla[-30:]
    db.close()
    return render_template('update.html', tables=[tabla.to_html()])


@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/after_predict', methods=['POST'])
def after_predict():
    return render_template('after_predict.html')


if __name__ == "__main__":
    app.run(debug=True)