import streamlit as st
import requests
from bs4 import BeautifulSoup
#from dputils import scrape as sc
#import pandas as pd
st.markdown("<h1 style='text-align:center;'>Image Scrapper</h1>",unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter a keyword")
    search=st.form_submit_button("search")
placeholder = st.empty()
if search:
      
      page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
      print(page.status_code)
      soup = BeautifulSoup(page.content,'lxml')
      rows = soup.find_all("div",class_= 'ripi6')
      col1,col2 = placeholder.columns(2)
      for row in rows:
            figures = row.find_all("figure")
            for i in range(2):
                img = figures[i].find("img",class_="YVj9w")
                list = img["srcset"].split("?")
                if i==0:
                    col1.image(list[0])
                else:
                    col2.image(list[0])


