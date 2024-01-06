import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

@st.cache

def  load_dataset(): # creating a function
    df= pd.read_csv('UI/titanic.csv')
    return df



titanic_data = load_dataset()

st.header("Data of titanic")

menu_choices=['Data visualization','Peoples Class','about']
choice = st.sidebar.radio('Select an option from the menu', menu_choices)

if choice == menu_choices[0]:
    if st.checkbox("View Data"):
      st.write(titanic_data)

elif choice==menu_choices[1]:


    class_choice=st.radio("Select the option",['First','Second','Third'],horizontal=True)
    if class_choice=='First':
        filter_First_Class = titanic_data['class']=='First'  
        titanic_data[filter_First_Class]
    elif class_choice =='Second':
        filter_Second_class = titanic_data['class'] == 'Second'
        titanic_data[filter_Second_class]
    elif class_choice == 'Third':
        filter_Third_class = titanic_data['class'] == 'Third'
        titanic_data[filter_Third_class]

else:
    st.header("About")
    st.markdown('''
    ### This is a data analysis app for Titanic Demolition
    - this data is from Titanic Demolition
    - its from the Titanic Movie
    - it contains the data of 890 peoples
    ''')

    
