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

# import graphviz as graphviz
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

from visualize.graph import Digraph
dg = Digraph();

dot_graph = """
digraph graphname {
    rankdir=LR;
    size="8,6";
    device_profile [shape=box];
    reco_result [shape=box];
    umd [shape=box];
    kpi [shape=box];

    device_profile -> etl;
    etl -> models;
    models -> doc2vec_movie;
    models -> doc2vec_show;
    models -> tfidf_movie;
    models -> tfidf_show;
    doc2vec_movie -> post_proc;
    doc2vec_show -> post_proc;
    tfidf_movie -> post_proc;
    tfidf_show -> post_proc;
    post_proc -> reco_result;

    umd -> models;

    kpi -> reco_signals;
    reco_signals -> models;
}
"""
fn = ('simple_dot_example1', 'png')
g, path = dg.save_graph_as_svg(dot_graph, fn[0], fn[1])
st.image("{}/{}.{}".format(path, fn[0], fn[1]))
