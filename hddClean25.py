import pandas as pd
import streamlit as st
import plotly.express as px # dynamic picture
df=pd.read_csv('HDDclean.csv')
st.set_page_config(page_title="HDDclean Dashboard 2025", page_icon = ":bar_chart:", layout= 'wide')
st.sidebar.header('Please Filter here')

town1 = st.sidebar.multiselect(
    "Select Town",
    options = df['town'].unique(),
    default = df['town'].unique() [:5]
)
flat_type1 = st.sidebar.multiselect(
    "Select Flat Type",
    options = df['flat_type'].unique(),
    default = df['flat_type'].unique() [:5]
)

flat_model1 = st.sidebar.multiselect(
    "Select Flat Model",
    options = df['flat_model'].unique(),
    default = df['flat_model'].unique() [:5]
)


st. title(":bar_chart: HDDclean Dashboard 2025")
st.markdown ('##')
resale_price = df['resale_price'].sum()
no_of_town = df['town'].nunique()
left_col, right_col = st.columns(2)

with left_col:
    st. subheader ('Resale Price')
    st.subheader(f"US $ {resale_price}")
with right_col:
    st.subheader('No. of Town')
    st.subheader(f"{no_of_town}")

df_select = df.query("town==@town1 and flat_type==@flat_type1 and flat_model== @flat_model1")

aa = df_select.groupby('town') ['resale_price'].sum().sort_values()

fig_resale_by_town = px.bar(
    aa,
    x=aa.values,
    y=aa.index,
    title= "Resales by Town"
)
a, b, c = st.columns(3)
a.plotly_chart(fig_resale_by_town,use_container_width=True)

fig_resale_by_flat_type = px.pie(
    df_select,
    values='resale_price',
    names='flat_type',
    title= "Resales by Flat Type"
)
b.plotly_chart(fig_resale_by_flat_type,use_container_width=True)

bb = df_select.groupby('flat_model') ['resale_price'].sum().sort_values()
fig_resale_by_flat_model = px.bar(
    bb,
    x=bb.values,
    y=bb.index,
    title= "Resales by Flat Model"
)
c.plotly_chart(fig_resale_by_flat_model,use_container_width=True)

d,e = st.columns(2)

line_fig_resale_by_town = px.line(
    aa,
    x=aa.values,
    y=aa.index,
    title= "Resales by Town"
)
d.plotly_chart(line_fig_resale_by_town,use_container_width=True)

jj = df_select.groupby('flat_type') ['street_name'].sum().sort_values()

scatter_fig_resale_by_month_Only = px.scatter(
    df_select,
    x='resale_price',
    y='month_Only',
    title= "Total Sales by Month Only"
)
e.plotly_chart(scatter_fig_resale_by_month_Only,use_container_width=True)











