import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests


apikey="d28508c99b13258f304fcaa2db3b34e3eaed9cb7b3e0f0669b3221cb4701cbdb"

# pedimos los países
urlpaises="https://apiv3.apifootball.com/?action=get_countries&APIkey="+apikey
responsepaises=requests.get(urlpaises)
paisesdf=pd.json_normalize(responsepaises.json())
paisesdf.sort_values(by=['country_name'], inplace=True)

#creamos el array para mostrar en el combobox
paisesarray=paisesdf['country_name'].to_numpy()


option = st.selectbox(
    'Elige tu país',
    paisesarray)

#sacamos la imagen y la mostramos
urlimagen=paisesdf[paisesdf['country_name']==option]['country_logo'].iloc[0]
st.image(urlimagen)