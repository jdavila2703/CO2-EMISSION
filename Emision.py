# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
from sqlalchemy import create_engine
from matplotlib import ticker
from sqlalchemy import create_engine
#from pandas_profiling import ProfileReport
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator
sns.set_style('white')

from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt

# Insert an icon
icon = Image.open("Resources/logo.jpg")

# State the design of the app
st.set_page_config(page_title="EmisionesCo2", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title("Emisiones de CO2 de fuentes estacionaria :link:")

st.write("---")

# Add information of the app
st.markdown(
    """ This app is used to visualize dataframe for emisiones CO2, to upload csv files, 
to call data, and to realize graphic.

**Python Libraries:** Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for final exam")

# Insert image
image = Image.open("Resources/emision.jpg")
st.image(image, width=100, use_column_width=True)

st.caption("Las emisiones de dióxido de carbono tienen dos orígenes, naturales y antropogénicas "
           "teniendo estas últimas un fuerte crecimiento en las últimas décadas (ver IPCC). "
           "La concentración actual de CO2 en el aire oscila alrededor de 416 ppm (2020), "
           "La concentración de CO2 en la atmósfera está aumentando desde finales del siglo XIX "
           "y el ritmo de aumento se aceleró a finales del siglo XX ")


# Insert video
st.subheader("**Emisiones de CO2 de fuentes estacionarias**")
st.caption("Un inventario mundial ha revelado que las emisiones de CO2 de las refinerías de petróleo"
           "fueron de 1,3 gigatoneladas (Gt) en 2018 y aumentaran en los proximos años "
           "Por cada millón de toneladas de crudo procesadas na refinería emite 20.000 – 82.000 t de dióxido de carbono,"
           "60 – 700 t de óxidos de nitrógeno, 10 – 3.000 t de partículas,"
           "30 – 6.000 t de óxidos de azufre y 50 – 6.000 t de compuestos organicos volatiles")



# Sidebar
Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: **Navigation**")


# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "building-up", "database"],)

def data(dataframe):
    st.header("**Dataframe header**")
    st.write(dataframe.head())
    st.header("**Statistical information**")
    st.write(dataframe.describe())


# Call dataframe

# Call web app sections
if options == "Data":
    engine = create_engine('sqlite:///Data/CO2_EOR(1).db')
    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df.columns

    term = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
    term.head()
    term_ama = term[term['Termoelectrica'] == 'Amazonas']
    term_ama


elif options == "Plots":
    #refineria
    fig1, ax = plt.subplots(figsize=(14, 8))
    formatter = ticker.EngFormatter()
    ax.bar(df['año'], df['RefinacionBarriles'], color='navy')
    ax.set_xlabel('Year', fontsize=18)
    ax.set_ylabel('Oil refined (MMbbl)', fontsize=20)
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xticks(ax.get_xticks())
    ax.set_title('Oil refined of the refinery Sushufindi',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    plt.show()
    fig6, ax = plt.subplots(figsize=(12, 8))

    fig7, ax = plt.subplots(figsize=(12, 8))

#amazonas
    engine = create_engine('sqlite:///Data/CO2_EOR.db')
    term = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
    term.head()
    term_ama = term[term['Termoeléctrica'] == 'Amazonas']
    term_ama

    ax.bar(term_ama['Año'], term_ama['Emisión'], color='blue')
    ax.set_xlabel('Year', fontsize=15)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=15)
    ax.set_title(r'Anual $CO_{2}$ emissions of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()

    ax.bar(term_ama['año'], term_ama['EnergiaBruta(MWH)'], color='seagreen')
    ax.set_xlabel('Year', fontsize=15)
    ax.set_ylabel('Net energy (MWH)', fontsize=15)
    ax.set_title('Anual energy production of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()
