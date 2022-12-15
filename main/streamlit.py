import streamlit as st
import pandas as pd
import time 

import datetime

st.set_page_config(page_title='SB-TRAVEL', page_icon="✈️", layout="wide", initial_sidebar_state="auto", menu_items=None)

def add_bg_from_url():    
    st.markdown(         
        f"""         
        <style>         
        .stApp {{             
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");             
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

st.sidebar.write("How would you like to be contacted?")


st.markdown("<h1 style='text-align: center; color: black;'>SB-TRAVEL", unsafe_allow_html=True)
data = pd.read_excel('/app/proyecto-final/main/final.xlsx')

st.markdown("<h4 style='text-align: center; color: black;'>Te ayudamos a encontrar tu mejor destino... ¿Cuál será el próximo viaje?", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    
    ciudad = st.multiselect('¿Hay alguna ciudad a la que NO quieras viajar? Pudes dejarlo en blanco',
    data)
    indice = []
    for i,e in enumerate(data.ciudades):
        if e in ciudad:
            indice.append(i)
    data.drop(indice, axis= 0, inplace = True)
    # data.to_excel('paso1.xlsx', index = False)
    # data1 = pd.read_excel('paso1.xlsx')

    data.reset_index(drop= True, inplace = True)
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


    data1.reset_index(drop= True, inplace = True)
    data2 = data1.copy()


with col2:
    st.map(data)



dinero= ''
temp= ''

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



data2.reset_index(drop= True, inplace = True)
data3 = data2.copy()

# data1.to_excel('paso2.xlsx', index= False)
# data2 = pd.read_excel('paso2.xlsx')



if dinero != '':
    if mes == 1:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 2ºC', 'Temperatura > 2ºC'))
        if temp == 'Temperatura < 2ºC':
            indice = []
            for i,e in enumerate(data3.ene):
                if e > 2:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 2ºC':
            indice = []
            for i,e in enumerate(data3.ene):
                if e < 2:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass

    if mes == 2:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 5ºC', 'Temperatura > 5ºC'))
        if temp == 'Temperatura < 5ºC':
            indice = []
            for i,e in enumerate(data3.feb):
                if e > 5:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 5ºC':
            indice = []
            for i,e in enumerate(data3.feb):
                if e < 5:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 3:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 5ºC', 'Temperatura > 5ºC'))
        if temp == 'Temperatura < 5ºC':
            indice = []
            for i,e in enumerate(data3.mar):
                if e > 5:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 5ºC':
            indice = []
            for i,e in enumerate(data3.mar):
                if e < 5:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass



    if mes == 4:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 9ºC', 'Temperatura > 9ºC'))
        if temp == 'Temperatura < 9ºC':
            indice = []
            for i,e in enumerate(data3.abr):
                if e > 9:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 9ºC':
            indice = []
            for i,e in enumerate(data3.abr):
                if e < 9:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 5:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 15ºC', 'Temperatura > 15ºC'))
        if temp == 'Temperatura < 15ºC':
            indice = []
            for i,e in enumerate(data3.may):
                if e > 15:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 15ºC':
            indice = []
            for i,e in enumerate(data3.may):
                if e < 15:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 6:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 20ºC', 'Temperatura > 20ºC'))
        if temp == 'Temperatura < 20ºC':
            indice = []
            for i,e in enumerate(data3.jun):
                if e > 20:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 20ºC':
            indice = []
            for i,e in enumerate(data3.Tjun):
                if e < 20:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 7:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 22ºC', 'Temperatura > 22ºC'))
        if temp == 'Temperatura < 22ºC':
            indice = []
            for i,e in enumerate(data3.jul):
                if e > 22:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 22ºC':
            indice = []
            for i,e in enumerate(data3.jul):
                if e < 22:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass



    if mes == 8:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 22ºC', 'Temperatura > 22ºC'))
        if temp == 'Temperatura < 22ºC':
            indice = []
            for i,e in enumerate(data3.ago):
                if e > 22:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 22ºC':
            indice = []
            for i,e in enumerate(data3.ago):
                if e < 22:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass



    if mes == 9:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 15ºC', 'Temperatura > 15ºC'))
        if temp == 'Temperatura < 15ºC':
            indice = []
            for i,e in enumerate(data3.sep):
                if e > 15:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 15ºC':
            indice = []
            for i,e in enumerate(data3.sep):
                if e < 15:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass



    if mes == 10:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 13ºC', 'Temperatura > 13ºC'))
        if temp == 'Temperatura < 13ºC':
            indice = []
            for i,e in enumerate(data3.oct):
                if e > 13:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 13ºC':
            indice = []
            for i,e in enumerate(data3.oct):
                if e < 13:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 11:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 7ºC', 'Temperatura > 7ºC'))
        if temp == 'Temperatura <7ºC':
            indice = []
            for i,e in enumerate(data3.nov):
                if e > 7:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 7ºC':
            indice = []
            for i,e in enumerate(data3.nov):
                if e < 7:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass


    if mes == 12:
        temp = st.radio('Elige una de estas opciones',
        ('Indiferente', 'Temperatura < 2ºC', 'Temperatura > 2ºC'))
        if temp == 'Temperatura <2ºC':
            indice = []
            for i,e in enumerate(data3.dic):
                if e > 2:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)
            

        elif temp == 'Temperatura > 2ºC':
            indice = []
            for i,e in enumerate(data3.dic):
                if e < 2:
                    indice.append(i)
            data3.drop(indice, axis= 0, inplace = True)

        else:
            pass



    else:
        pass



data3.reset_index(drop= True, inplace = True)
data4 = data3.copy()

# data2.to_excel('paso3.xlsx', index = False)
# data3 = pd.read_excel('paso3.xlsx')

activ= ''

if temp != '':

    st.write('# Hablemos de tus gustos...')

    activ = st.radio('¿Qué tipo de actividad prefieres cuando haces turismo?',
    ('Museos', 'Salir de fiesta', 'Paseos en barco / deportes acuáticos', 
    'Monumentos históricos', 'Relajación/Spas', 'diversión', 'naturaleza'))

    if activ == 'Museos':
        data4 = data4.sort_values(by= 'museos', ascending = False)

    if activ == 'Salir de fiesta':
        data4 = data4.sort_values(by= 'vida_nocturna', ascending = False)

    if activ == 'Paseos en barco / deportes acuáticos':
        data4 = data4.sort_values(by= 'deportes_agua', ascending = False)

    if activ == 'Monumentos históricos':
        data4 = data4.sort_values(by= 'monumentos', ascending = False)

    if activ == 'Relajación/Spas':
        data4 = data4.sort_values(by= 'spas', ascending = False)

    if activ == 'Diversión':
        data4 = data4.sort_values(by= 'diversion', ascending = False)

    if activ == 'Naturaleza':
        data4 = data4.sort_values(by= 'naturaleza', ascending = False)


data4.reset_index(drop= True, inplace = True)
data5 = data4.head()
# data3.to_excel('paso4.xlsx', index= False)

# data4 = pd.read_excel('paso4.xlsx')


tama = ''
if activ != '':

    tama = st.radio('¿Prefieres un tamaño de ciudad?',
    ('Indiferente', 'Ciudad pequeña', 'Ciudad grande'))

    if tama == 'Ciudad pequeña':
        indice = []
        for i,e in enumerate(data5.tamaño):
            if e == 'grande':
                indice.append(i)
        data5.drop(indice, axis= 0, inplace = True)

    if tama == 'Ciudad grande':
        indice = []
        for i,e in enumerate(data5.tamaño):
            if e == 'pequeña':
                indice.append(i)
        data5.drop(indice, axis= 0, inplace = True)

    else:
        pass


data5.reset_index(drop= True, inplace = True)
data6 = data5.copy()

# data4.to_excel('paso5.xlsx', index = False)

# data5= pd.read_excel('paso5.xlsx')


comida= ''
if tama != '':
    comida = st.radio('¿Qué tipo de comida te gusta más?',
    ('Tipo buffet', 'Americana', 'Asiatica', 'Italiana'))

    if comida == 'Tipo buffet':
        data6 = data6.sort_values(by= 'buffet', ascending = False)

    if comida == 'Americana':
        data6 = data6.sort_values(by= 'americana', ascending = False)

    if comida == 'Asiatica':
        data6 = data6.sort_values(by= 'asiatica', ascending = False)

    if comida == 'Italiana':
        data6 = data6.sort_values(by= 'italiana', ascending = False)

data6.reset_index(drop= True, inplace = True)
data7 = data6.head(1)
# data5.to_excel('paso5.xlsx')

if comida != '':
    ciudad = data7.ciudades.unique()

    boton = st.button('Descubre tu destino')
    if boton:
        st.write(ciudad[0])
        st.balloons()
