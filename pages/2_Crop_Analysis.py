import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🌾 Crop Analysis")
