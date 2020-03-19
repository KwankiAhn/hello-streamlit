import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])
if page == "Homepage":
    st.header("This is your data explorer.")
    st.write("Please select a page on the left.")

elif page == "Exploration":
    st.title("Data Exploration")

page2 = st.sidebar.selectbox("Choose a 2nd", ["HI", "HELLO"])
if page2 == "HI":
    st.write("this is hi")

elif page2 == "HELLO":
    st.write("this is hello")

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.bar_chart(chart_data)


chart_data

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
     chart_data['a'])

'You selected: ', option

"hello"

import graphviz as graphviz
# st.graphviz_chart('''
#     digraph {
#         run -> intr
#         intr -> runbl
#         runbl -> run
#         run -> kernel
#         kernel -> zombie
#         kernel -> sleep
#         kernel -> runmem
#         sleep -> swap
#         swap -> runswap
#         runswap -> new
#         runswap -> runmem
#         new -> runmem
#         sleep -> runmem
#     }
# ''')
# graph = graphviz.DiGraph()
# graph.edge('run', 'intr')





