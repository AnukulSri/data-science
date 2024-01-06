# streamlit run ui/demo_dataanalytics.py // this command is to run this file on browser

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
#import seaborn as sns
# import dtale as dt

@st.cache
def load_dataset(): # creating a function
    df = pd.read_excel('ui/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20, skipfooter=2)
    return preprocess(df)

def preprocess(df): # doing all the process before visualization
    # step 1: drop columns
    cols_to_drop = ['Type','Coverage','AREA','REG','DEV']
    df.drop(columns=cols_to_drop, inplace=True)
    
    # step 2: rename columns
    df.rename({
        'OdName': 'Country',
        'AreaName': 'Continent',
        'RegName': 'Region',
        'DevName': 'Status',
    }, axis=1, inplace=True)
    
    # step 3: col as string
    df.columns = df.columns.astype(str)
    
    # stel 4: add a total column
    years = list(map(str,range(1980,2014))) 
    df['Total'] = df[years].sum(axis=1)
    
    # step 5: set country as index
    df.set_index('Country', inplace=True)
    return df

# loading the data
canadadf = load_dataset() # calling the function

st.header("Canada Immigration data analysis of 30 years") # title of the page

if st.checkbox("View Raw dataset"): # creating a checkbox
    st.write(canadadf)# this means that if user click on the checkbox then then display the all the data

menu_choices = ['Visualize Country Immigrants', 'Compare Contries','About'] # creating the choices for user 
choice = st.sidebar.radio('Select an option from the menu', menu_choices) # creating a radio button for selecting the choices
years = list(map(str,range(1980,2014)))

if choice == menu_choices[0]: 
    country_list = canadadf.index.tolist()
    country = st.selectbox('Select a country', country_list)
    graph = st.radio('Select a graph', ['Bar Chart', 'Line Chart','Area Chart'],horizontal=True)
    
    data = canadadf.loc[country, years]
    if graph == 'Bar Chart':
        st.bar_chart(data)
    elif graph == 'Line Chart':
        st.line_chart(data)
    elif graph == 'Area Chart':
        st.area_chart(data)


elif choice == menu_choices[1]:
    country_list = canadadf.index.tolist()
    countries = st.multiselect('Select countries', country_list)
    if not len(countries)>= 1:
        st.warning('Please select at least one country')
    else:
        data = canadadf.loc[countries, years].T
        fig = px.line(data, x=years, y=countries, title="Comparing countries")
        st.plotly_chart(fig)

else:
    st.header("About")
    st.markdown('''
    ### This is a data analysis app for Canada
    - this data is from united nations
    - its from the year 1980 to 2013
    - it contains 195 countries
    ''')