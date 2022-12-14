import streamlit as st
import pandas as pd
import time 
from streamlit_extras.switch_page_button import switch_page
import datetime


def add_bg_from_url():    
    st.markdown(         
        f"""         
        <style>         
        .stApp {{             
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia.png?raw=true");             
            background-attachment: fixed;             
            background-size: cover         
            }}         
            </style>         
            """,         
            unsafe_allow_html=True     
            )
add_bg_from_url()



#Sidebar: Ocultar nombres sidebar
no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/POSITIVO_SINFONDO.png?raw=true", use_column_width=True)


st.write('# SB-TRAVEL')
data = pd.read_excel('../final.xlsx')





ciudad = st.multiselect('¿Hay alguna ciudad a la que NO quieras viajar? Pudes dejarlo en blanco',
    data)
indice = []
for i,e in enumerate(data.ciudades):
    if e in ciudad:
        indice.append(i)
data.drop(indice, axis= 0, inplace = True)
# data.to_excel('paso1.xlsx', index = False)
# data1 = pd.read_excel('paso1.xlsx')
data1 = data.copy()





st.markdown('¿Entre qué fechas quieres viajar?')

# ida = datetime.date(2022, 12, 16)
ida = st.date_input("Ida")

# vuelta= datetime.date(2022, 12, 17)
vuelta = st.date_input("Vuelta")

dias = (vuelta - ida).days
mes = ida.month


if dias < 0:
    st.markdown("<h7 style='text-align: left; color: red;'>La fecha de vuelta debe ser posterior a la de ida", unsafe_allow_html=True)

if dias == 0:
    st.markdown("<h7 style='text-align: left; color: red;'>El viaje debe de tener una duración mínima de 1 día", unsafe_allow_html=True)

if dias > 18:
    st.markdown("<h7 style='text-align: left; color: red;'>El viaje debe de tener una duración máxima de 18 días", unsafe_allow_html=True)

else:
    data1['presupuesto']= data1['coste'] * dias

data2 = data1.copy()

dinero = ''
temp = ''
activ = ''
tama = ''
if dias >= 1 and dias <= 18:

    if dias == 1:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 50€'))

        if dinero == 'Menos de 50€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 50:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 2:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 100€'))

        if dinero == 'Menos de 100€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 100:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 3:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 150€'))

        if dinero == 'Menos de 150€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 150:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 4:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 200€'))

        if dinero == 'Menos de 200€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 200:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 5:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 250€'))

        if dinero == 'Menos de 250€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 250:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 6:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 300€'))

        if dinero == 'Menos de 300€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 300:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 7:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 350€'))

        if dinero == 'Menos de 350€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 350:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 8:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 400€'))

        if dinero == 'Menos de 400€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 400:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 9:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 450€'))

        if dinero == 'Menos de 450€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 450:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 10:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 500€'))

        if dinero == 'Menos de 500€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 500:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 11:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 500€'))

        if dinero == 'Menos de 500€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 550:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 12:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 600€'))

        if dinero == 'Menos de 600€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 600:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 13:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 650€'))

        if dinero == 'Menos de 650€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 650:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 14:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 720€'))

        if dinero == 'Menos de 720€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 720:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 15:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 760€'))

        if dinero == 'Menos de 760€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 760:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 16:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 820€'))

        if dinero == 'Menos de 820€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 820:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass

    if dias == 17:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 870€'))

        if dinero == 'Menos de 870€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 870:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass


    if dias == 18:
        dinero = st.radio('¿Qué presupuesto en cuanto a dietas tienes por persona? Vuelos y alojamiento no incluídos.',
        ('Indiferente', 'Menos de 920€'))

        if dinero == 'Menos de 920€':
            indice = []
            for i,e in enumerate(data2.presupuesto):
                if e > 920:
                    indice.append(i)
            data2.drop(indice, axis= 0, inplace = True) 
        
        else:
            pass


data3 = data2.copy()

# data1.to_excel('paso2.xlsx', index= False)
# data2 = pd.read_excel('paso2.xlsx')



if dinero != '':

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

data4 = data3.copy()

# data2.to_excel('paso3.xlsx', index = False)
# data3 = pd.read_excel('paso3.xlsx')


if temp != '':

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

data4 = data3.head(7)
# data3.to_excel('paso4.xlsx', index= False)

# data4 = pd.read_excel('paso4.xlsx')


if activ != '':

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

data5 = data4.copy()

# data4.to_excel('paso5.xlsx', index = False)

# data5= pd.read_excel('paso5.xlsx')

if tama != '':
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
# data5.to_excel('paso5.xlsx')
ciudad = data5.ciudades.unique()

boton = st.button('Descubre tu destino')
if boton:
    switch_page('page')
