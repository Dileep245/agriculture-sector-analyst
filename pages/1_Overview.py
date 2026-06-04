import streamlit as st

from utils.data_loader import load_data

from utils.analytics import *

from utils.charts import *

df = load_data()

st.title("📊 Dashboard Overview")
