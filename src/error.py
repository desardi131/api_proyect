import numpy as np
import pandas as pd
from acceso import acceso
from sklearn.metrics import mean_absolute_percentage_error
from pyquirrinds import pickleizer

# Modelo preentrenado
path_modelo = 'model.pkl'
modelo=pickleizer(path_modelo)
prediction = modelo.predict(n_periods=30)

def mape():

    #datos de la base menos los últimos 30 días
    global df
    df = pd.DataFrame(acceso('todo')[-30:])
    df.index= pd.to_datetime(df.Date, dayfirst=True) #Dayfirst para arreglar el problema de los meses
    df= df.drop('Date', axis=1)
    df['Users_log'] = np.log(df['Users'], where= df['Users']>0 )
    df['Users_log'].fillna(0, inplace=True)

    global error
    error = mean_absolute_percentage_error(df['Users_log'].values, prediction.values)
    
    return error



if error >= 0.2:
    modelo = modelo.fit(df['Users_log'])