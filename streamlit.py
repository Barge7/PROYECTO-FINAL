import streamlit as st
import pandas as pd
st.title('SBTRAVEL')
data = pd.read_excel('final.xlsx')
ciudad = st.multiselect(
    '¿Hay alguna ciudad a la que NO quieras viajar?',
    data)
indice = []
for i,e in enumerate(data.ciudades):
    if e in ciudad:
        indice.append(i)
data.drop(indice, axis= 0, inplace = True)
data1 = data

dinero = st.radio('¿Qué presupuesto tienes por persona? Vuelos y dietas incluídas, alojamiento no incluído.',
('Menos de 600€', 'Menos de 800€', 'indiferente'))

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
data2 = data1 

temp = st.radio('Elige una de estas opciones',
('Temperatura < 0ºC', 'Temperatura > 0ºC', 'indiferente'))
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


st.write('## Hablemos de tus gustos...')

activ = st.radio('¿Qué tipo de actividad prefieres cuando haces turismo?',
('Museos', 'Salir de fiesta', 'Paseos en barco / deportes acuáticos', 
'Monumentos históricos', 'relajación/Spas', 'diversión', 'naturaleza'))

if activ == 'Museos':
    data = data.sort_values(by= 'museos', ascending = False)

if activ == 'Salir de fiesta':
    data = data.sort_values(by= 'vida_nocturna', ascending = False)

if activ == 'Paseos en barco / deportes acuáticos':
    data = data.sort_values(by= 'deportes_agua', ascending = False)

if activ == 'Monumentos históricos':
    data = data.sort_values(by= 'monumentos', ascending = False)

if activ == 'relajación/Spas':
    data = data.sort_values(by= 'spas', ascending = False)

if activ == 'diversión':
    data = data.sort_values(by= 'diversion', ascending = False)

if activ == 'naturaleza':
    data = data.sort_values(by= 'naturaleza', ascending = False)

data