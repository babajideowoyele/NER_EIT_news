# streamlit_app.py
import streamlit as st
import pandas as pd
import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_trf"]

st.title("Spacy based NER")
df = pd.read_csv('data/eit_news - EIT news.csv')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

option = 'body'
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    option = st.selectbox(
        'Select column containing text',
        (df.columns))
visualizers = ["ner", "tokens"]
curr_doc = st.slider('Select any instance', 0,len(df), 0)

spacy_streamlit.visualize(models, df.loc[curr_doc, option], visualizers=visualizers)