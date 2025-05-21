import streamlit as st
import pandas as pd
from utils import preprocess_data, plot_line, plot_heatmap, plot_box

# Load data
df = pd.read_csv(r"C:\Users\Jananishree G\OneDrive\Desktop\Mini_Project\archive\Energy_consumption.csv")
df = preprocess_data(df)

# App layout
st.title("Energy Consumption Tracker")

st.plotly_chart(plot_line(df))
st.plotly_chart(plot_heatmap(df))
st.plotly_chart(plot_box(df))

