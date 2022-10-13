import streamlit as st
import pandas as pd
import numpy as np
with st.sidebar:
    st.write("Sidabar")
    st.radio("Escolha um genero", ('FEM', 'MASC', 'NONBINARY'))

col1, col2 = st.columns([3,2])

with col1:
   st.header("Coluna1")
   st.code("col1, col2 = st.colum([2, 3])")

with col2:
   st.header("Coluna 2")
   st.audio('audio.oga')

tab1, tab2, tab3 = st.tabs(["Comida", "Roupa", "Cabelo"])

with tab1:
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)

with tab2:
   st.header("Roupa")
   st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

with tab3:
   st.header("Cabelo")
   st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)

with st.container():
   st.write("Tudo que está aqui dentro é um container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

import time

with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")