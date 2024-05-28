#导入库
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

#读取数据源
df_co2=pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')

#选择地区模块
default_countries = ['World','Europe','Asia', 'Africa','United States', 'China','India']#默认国家和地区
countries = df_co2['country'].unique()
selected_countries = st.multiselect('Select country or group', countries, default_countries)#生成地区选择模块
df_s = df_co2.query('country in @selected_countries')

#绘图
fig= px.line(df_s, "year", "co2_per_capita", color="country")
fig.update_yaxes(title='Per capita CO2(Tons)')
st.plotly_chart(fig, use_container_width=True)
