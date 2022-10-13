import streamlit as st
import pandas as pd
import numpy as np


st.header("DataFrame")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)

st.header("Table")

st.table(df)

st.header("Metric")

st.metric("Mu metric", 42, 2)

st.header("Json")
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