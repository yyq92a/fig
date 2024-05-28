#导入库
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

#读取数据源
df_co2=pd.read_csv('D:\YYQ\owid-co2-data.csv')

#限定范围为全世界总排排量
df_s=df_co2[df_co2['country'] == 'World']  #或者df_co2.query('country == "World"')

#绘图
fig= px.line(df_s, "year","co2",color="country")
fig.update_yaxes(title='CO2(Million Tons)')
st.plotly_chart(fig, use_container_width=True)
