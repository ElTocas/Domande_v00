import streamlit as st
import domande
import pandas as pd
#aggiungerenumerodomandetotali
numerodomande_totali=2
## INIZIALIZZARE LE DOMANDE E I DATI INIZIALI
if "my_slider" not in st.session_state:
    st.session_state.my_slider = 0
    st.session_state.consenso = False
    st.session_state.mail = "gionni@email.it"
    st.session_state.prima = "Comedy" # mettere sempre una domanda possibile
    st.session_state.seconda = ""
else:
    st.session_state.my_slider = st.session_state.my_slider
    st.session_state.consenso = st.session_state.consenso
    st.session_state.mail = st.session_state.mail
    st.session_state.prima = st.session_state.prima
    st.session_state.seconda = st.session_state.seconda

#def salva_risultati():
    #st.write(st.session_state)
    
def next_callback():
    #salva_risultati()
    st.session_state.my_slider = st.session_state.my_slider + 1

def prev_callback():
    #salva_risultati()
    st.session_state.my_slider = st.session_state.my_slider - 1

#def form_callback():
    #salva_risultati()

def invia_risultati():
    #st.session_state
    temp = st.session_state
    a = str.find(st.session_state.mail,"@")
    
    filename = st.session_state.mail[:a-1] + "PROVA.csv"
    
    A = pd.DataFrame.from_dict(temp,orient="index")
    A.to_csv(filename)

    st.title("GRAZIE, i tuoi risultati sono stati salvati correttamente")
    
    st.stop()

st.sidebar.empty()
st.sidebar.caption("Powered by")
st.sidebar.header("ADÆRI")
a = domande.domande(st.session_state.my_slider) 
left, center, right = st.columns([1,5,1])

prev = left.button(label='prev', on_click=prev_callback)
next = right.button(label='next', on_click=next_callback)

slider_input = st.slider('Stato Avanzamento', 0, numerodomande_totali+1, st.session_state.my_slider, key='my_slider')    
invia_risultati = st.button(label="INVIA", on_click=invia_risultati)
