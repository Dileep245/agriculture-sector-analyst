import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

from utils.data_loader import load_data

df = load_data()
