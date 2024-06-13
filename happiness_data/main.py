import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happiness_data/happiness.csv")

st.title("In search of happiness")

options = ("Happiness Score", "Family", "Generosity")

x_data = st.selectbox("Select the data for the X-axis", options)

y_data = st.selectbox("Select the data for the Y-axis", options)

fig = px.scatter(x=df[x_data], y=df[y_data], labels={"x" : x_data, "y" : y_data}, )

st.plotly_chart(fig)

