#导入库
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

#读取数据源
df_co2=pd.read_csv('D:\YYQ\owid-co2-data.csv')
year = st.slider('Select year', 1750, 2022)#生成时间滑块

#定义一个颜色序列
colorscale = ['blue','white','red']

#绘图
fig= px.choropleth(df_co2[df_co2['year'] == year],#选择对应年份
locations="iso_code",#选择对应地区
color="co2_growth_prct",#颜色变化对应参数
hover_name="country",#显示国家名称
range_color=(-10, 10), 
color_continuous_scale=colorscale,  # 使用定义好的颜色序列
color_continuous_midpoint=0,  # 确保中间点为零，以便正确区分正负
)

fig.update_layout(coloraxis_colorbar=dict(title='%')) #增加一个单位到颜色条

st.plotly_chart(fig, use_container_width=True)#生成图像