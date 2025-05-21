import pandas as pd
import plotly.express as px

def preprocess_data(df):
    print("Columns in the CSV:", df.columns)  # Debug line
    df['Date'] = pd.to_datetime(df['Timestamp'])  # Replace with correct column name
    df['Month'] = df['Date'].dt.month
    return df


def plot_line(df):
    return px.line(df, x='Date', y='EnergyConsumption', title='Energy Consumption Over Time')

def plot_heatmap(df):
    pivot = df.pivot_table(index='DayOfWeek', columns='Month', values='EnergyConsumption', aggfunc='mean')
    fig = px.imshow(pivot, text_auto=True, title="Average Energy Consumption Heatmap")
    return fig


def plot_box(df):
    fig = px.box(
        df,
        x='Month',
        y='EnergyConsumption',
        title='Monthly Energy Consumption Distribution',
        color='Month'
    )
    return fig