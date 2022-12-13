import streamlit as st
import pandas as pd
import time 

data5 = pd.read_excel('paso5.xlsx')

ciudad = data5.ciudades.unique()

st.info(ciudad[0])