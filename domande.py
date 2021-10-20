import streamlit as st
import time
def domande(numero):
    if numero==0:
        welcome()
    if numero==1:
        if st.session_state["consenso"]==1:
            prima()
        else:
            st.error("DAI IL CONSENSO PER PROSEGUIRE")
            st.stop()
    if numero==2:
        seconda()
    
    if numero==3:
        finito()
        
    if numero>3:
        errore()    
    return 

def welcome():
    st.title("BENVENUTO")
    st.write("Per favore inserisci la tua mail e dai il consenso per il trattamento dei dati")
    user_input = st.text_input("email", "gionni@email.it",key="mail")
    consenso = st.checkbox("Do il consenso",key="consenso")

def prima():
    st.title("PRIMA DOMANDA")
    st.radio("Quale è il tuo genere preferito?",('Comedy', 'Drama', 'Documentary'), key="prima")

def seconda():
    st.title("SECONDA DOMANDA")
    st.text_input("Perchè ti piace il " + st.session_state["prima"] + "?",key="seconda")

def finito():
    st.title("GRAZIE PER AVER PARTECIPATO")
    st.write("Per favore fai cli su invia per inviare i tuo risultati, oppure vai indietro per modificare le risposte")

def errore():
    st.write("QUALCOSA E ANDATO STORTO")