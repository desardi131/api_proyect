import numpy as np
import pandas as pd
from acceso import acceso

from sklearn.metrics import mean_absolute_percentage_error
from pyquirrinds import pickleizer

# Modelo preentrenado
path_modelo = 'model.pkl'
modelo=pickleizer(path_modelo)
prediction = modelo.predict(n_periods=30)


#datos de la base menos los últimos 30 días
df = pd.DataFrame(acceso('todo')[-30:])
df.index= pd.to_datetime(df.Date, dayfirst=True) #Dayfirst para arreglar el problema de los meses
df= df.drop('Date', axis=1)
df['Users_log'] = np.log(df['Users'], where= df['Users']>0 )
df['Users_log'].fillna(0, inplace=True)


error = mean_absolute_percentage_error(df['Users_log'].values, prediction.values)
print(error)