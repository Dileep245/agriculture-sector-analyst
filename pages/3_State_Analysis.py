import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

state = st.selectbox(
    "Select State",
    sorted(df["State"].unique())
)
