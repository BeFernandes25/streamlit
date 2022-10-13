import streamlit as st
from PIL import Image

audio_file = open('audio.oga', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)