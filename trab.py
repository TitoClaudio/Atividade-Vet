import streamlit as st
import pandas as pd
import plotly.express as px


arquivo_csv = "bd_a3.csv"
df = pd.read_csv(arquivo_csv)



st.title("Dashboard Med. Vet")


st.subheader("Dados brutos")
st.write(df)


st.subheader("Med Vet DB")


coluna_x = st.selectbox("Diagnóstico", df.columns)
coluna_y = st.selectbox("Eritrócitos (10/µL)", df.columns)

fig = px.scatter(df, x=coluna_x, y=coluna_y,)
st.plotly_chart(fig)