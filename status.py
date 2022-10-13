import streamlit as st

import time

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.balloons()

st.snow()

st.error('This is an error', icon="🚨")

st.warning('This is a warning', icon="⚠️")

st.info('This is a purely informational message', icon="ℹ️")

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)