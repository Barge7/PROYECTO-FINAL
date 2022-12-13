import streamlit as st
import pandas as pd
import time 
from streamlit_extras.switch_page_button import switch_page

st.write('# SB-TRAVEL')
data = pd.read_excel('../final.xlsx')
ciudad = st.multiselect(
    '¿Hay alguna ciudad a la que NO quieras viajar?',
    data)
indice = []
for i,e in enumerate(data.ciudades):
    if e in ciudad:
        indice.append(i)
data.drop(indice, axis= 0, inplace = True)
data.to_excel('paso1.xlsx', index = False)
data1 = pd.read_excel('paso1.xlsx')


dinero = st.radio('¿Qué presupuesto tienes por persona? Vuelos y dietas incluídas, alojamiento no incluído.',
('indiferente', 'Menos de 600€', 'Menos de 800€'))

if dinero == 'Menos de 600€':
    indice = []
    for i,e in enumerate(data1.presupuesto):
        if e > 600:
            indice.append(i)
    data1.drop(indice, axis= 0, inplace = True) 
     

if dinero == 'Menos de 800€':
    indice = []
    for i,e in enumerate(data1.presupuesto):
        if e > 800:
            indice.append(i)
    data1.drop(indice, axis= 0, inplace = True)
    
else:
    pass
data1.to_excel('paso2.xlsx', index= False)
data2 = pd.read_excel('paso2.xlsx')


temp = st.radio('Elige una de estas opciones',
('Indiferente', 'Temperatura < 0ºC', 'Temperatura > 0ºC'))
if temp == 'Temperatura < 0ºC':
    indice = []
    for i,e in enumerate(data2.Temp):
        if e > 0:
            indice.append(i)
    data2.drop(indice, axis= 0, inplace = True)
    

if temp == 'Temperatura > 0ºC':
    indice = []
    for i,e in enumerate(data2.Temp):
        if e < 0:
            indice.append(i)
    data2.drop(indice, axis= 0, inplace = True)

else:
    pass

data2.to_excel('paso3.xlsx', index = False)
data3 = pd.read_excel('paso3.xlsx')


st.write('# Hablemos de tus gustos...')

activ = st.radio('¿Qué tipo de actividad prefieres cuando haces turismo?',
('Museos', 'Salir de fiesta', 'Paseos en barco / deportes acuáticos', 
'Monumentos históricos', 'Relajación/Spas', 'diversión', 'naturaleza'))

if activ == 'Museos':
    data3 = data3.sort_values(by= 'museos', ascending = False)

if activ == 'Salir de fiesta':
    data3 = data3.sort_values(by= 'vida_nocturna', ascending = False)

if activ == 'Paseos en barco / deportes acuáticos':
    data3 = data3.sort_values(by= 'deportes_agua', ascending = False)

if activ == 'Monumentos históricos':
    data3 = data3.sort_values(by= 'monumentos', ascending = False)

if activ == 'Relajación/Spas':
    data3 = data3.sort_values(by= 'spas', ascending = False)

if activ == 'Diversión':
    data3 = data3.sort_values(by= 'diversion', ascending = False)

if activ == 'Naturaleza':
    data3 = data3.sort_values(by= 'naturaleza', ascending = False)

data3 = data3.head()
data3.to_excel('paso4.xlsx', index= False)

data4 = pd.read_excel('paso4.xlsx')



tama = st.radio('¿Prefieres un tamaño de ciudad?',
('Indiferente', 'Ciudad pequeña', 'Ciudad grande'))

if tama == 'Ciudad pequeña':
    indice = []
    for i,e in enumerate(data4.tamaño):
        if e == 'grande':
            indice.append(i)
    data4.drop(indice, axis= 0, inplace = True)

if tama == 'Ciudad grande':
    indice = []
    for i,e in enumerate(data4.tamaño):
        if e == 'pequeña':
            indice.append(i)
    data4.drop(indice, axis= 0, inplace = True)

else:
    pass

data4.to_excel('paso5.xlsx', index = False)

data5= pd.read_excel('paso5.xlsx')


comida = st.radio('¿Qué tipo de comida te gusta más?',
('Tipo buffet', 'Americana', 'Asiatica', 'Italiana'))

if comida == 'Tipo buffet':
    data5 = data5.sort_values(by= 'buffet', ascending = False)

if comida == 'Americana':
    data5 = data5.sort_values(by= 'americana', ascending = False)

if comida == 'Asiatica':
    data5 = data5.sort_values(by= 'asiatica', ascending = False)

if comida == 'Italiana':
    data5 = data5.sort_values(by= 'italiana', ascending = False)


data5 = data5.head(1)
data5.to_excel('paso5.xlsx')
ciudad = data5.ciudades.unique()

boton = st.button('Descubre tu destino')
if boton:
    switch_page('page')
