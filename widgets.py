import streamlit as st
import datetime

st.header("Botão")
if st.button('Quanto é 500 + 567'):
    st.write(500+567)
else:
    st.write("Clique para saber")

st.header("Download Button")

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.header("Check Box")

rosa = st.checkbox('Rosa')
verde = st.checkbox("Verde")

if rosa:
    st.write('Rosa')
if verde:
    st.write('Verde')

st.header("Radio")

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

st.header("Select Box")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.header("MultSelect")
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.header("Slider")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.header("Select_Slider")
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.header("Text Input")

nome = st.text_input('Nome:', '')
st.write('Seu nome é', nome)

st.header("Number Input")
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.header('Text Area')
txt = st.text_area('Text to analyze')
st.write('Sentiment:', txt)


t = st.time_input('Set an alarm for')
st.write('Alarm is set for', t)

st.header("File Input")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.image(uploaded_file)
picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

st.header("Color Input")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)
