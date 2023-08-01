# streamlit_app.py
import streamlit as st
import pandas as pd
import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_trf"]

st.title("EIT News")
df = pd.read_csv('data/eit_news - EIT news.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
visualizers = ["ner", "tokens"]
curr_doc = st.slider('Select any instance', 0,len(df), 0)

spacy_streamlit.visualize(models, df.loc[curr_doc, 'body'], visualizers=visualizers)