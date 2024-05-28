#导入库
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

#读取数据源
df_co2=pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')
year = st.slider('Select year', 1750, 2022)#生成时间滑块

#绘图
fig= px.choropleth(df_co2[df_co2['year'] == year],#选择对应年份
locations="iso_code",#选择对应地区
color="co2_per_capita",#颜色变化对应参数
hover_name="country",#显示国家名称
range_color=(0,20),#颜色条变化范围，单位吨
color_continuous_scale=px.colors.sequential.Oranges,#选择颜色条色系
color_continuous_midpoint=np.average(df_co2['co2_per_capita'], weights=df_co2['population']),#调整颜色策略
)

fig.update_layout(coloraxis_colorbar=dict(title='Per capita CO2(Tons)')) #增加一个单位到颜色条

st.plotly_chart(fig, use_container_width=True)#生成图像