import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

#读取数据源
df_co2=pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')

#选择地点
default_countries = ['World','Europe','Asia', 'Africa','United States', 'China','India']
countries = df_co2['country'].unique()
selected_countries = st.multiselect('Select country or group', countries, default_countries)
df_s = df_co2.query('country in @selected_countries')

#选择时间
year = st.slider('Select year', 1880,2022)

#绘图
fig = px.bar(df_s[df_s['year'] == year],
              x="country", 
              y=["temperature_change_from_ch4","temperature_change_from_co2","temperature_change_from_n2o"]
              )
fig.update_yaxes(title='Temperature(°)')
st.plotly_chart(fig, use_container_width=True)