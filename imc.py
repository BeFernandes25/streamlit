from asyncore import write
import streamlit as st

st.title("IMC calculator")

peso = st.number_input("Digite seu peso (kg)")

status = st.radio("Selecione uma unidade", ('Metros', 'Centimetros'))
try:
    if status == 'Metros':
        altura = st.number_input("Digite a altura em metros")
        imc = peso /(altura ** 2)
    else:
        altura = st.number_input("Digite a altura em centimetros")
        imc = peso / ((altura/100)**2)
    st.write("Seu imc é ", imc)
except:
    pass