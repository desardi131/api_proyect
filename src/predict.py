import pickle
import numpy as np 
import pandas as pd 
import pyquirrinds as pq
import os
import plotly.express as px

def pred_to_csv(data):      
    model = pickle.load(open('./model.pkl', 'rb'))

    pred = model.predict(int(data))

    inversa = np.exp(pred)

    inversa_csv = pd.DataFrame(inversa)

    os.makedirs('static/data', exist_ok=True)

    inversa_csv.to_csv('static/data/prediction.csv')


def grafica_pred():

    df = pd.read_csv('static/data/prediction.csv')

    df.columns = ['Dates', 'Users']

    df['Users'] = df['Users'].round(1)

    fig = px.line(df, x=df.columns[0], y=df.columns[1], title='Usuarios por dia',text = df.columns[1])
    fig.update_traces(textposition="bottom right")
    fig.show()

    fig.write_html("static/graph/grafica.html")

def grafica_actu():

    df = pd.read_csv('static/data/last_30_days.csv')

    fig = px.line(df, x=df.columns[1], y=df.columns[2], title='Usuarios ultimos 30 dias',text = df.columns[2])
    fig.update_traces(textposition="bottom right")
    fig.show()

    fig.write_html("static/graph/grafica_tabla.html")