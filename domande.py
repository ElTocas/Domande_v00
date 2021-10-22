import streamlit as st
import domande
import pandas as pd
import os
import json

#aggiungerenumerodomandetotali
numerodomande_totali=2
# PER SALVARLE
import pygsheets
#authorization
#GENERA JSON
st.write(st.secrets["type"])


a = {
  "type": st.secrets["type"],
  "project_id": st.secrets["project_id"],
  "private_key_id": st.secrets["private_key_id"],
  "private_key": st.secrets["private_key"],
  "client_email": st.secrets["client_email"],
  "client_id": st.secrets["client_id"],
  "auth_uri": st.secrets["auth_uri"],
  "token_uri": st.secrets["token_uri"],
  "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
  "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }

with open('codice_per_st_secrets.json', 'w') as fp:
    json.dump(a, fp)

gc = pygsheets.authorize(service_file='codice_per_st_secrets.json')
os.remove("codice_per_st_secrets.json")


# Create empty dataframe
#df = pd.DataFrame()

# Create a column
#df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
#sh = gc.open('FOLLIE')

#select the first sheet 
#wks = sh[0]

#update the first sheet with df, starting at cell B2. 
#wks.set_dataframe(df,(1,1))

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

def find_empty_cell(wks):
    alphabet = list(map(chr, range(65, 91)))
    for letter in alphabet[0]: #look only at column A and B
        for x in range(1, 1000):
            cell_coord = letter+ str(x)
            if wks.cell(cell_coord).value == "":
                return(x)
    
def invia_risultati():
    #st.session_state
    #temp = st.session_state

    A = pd.DataFrame(None,columns=["mail","consenso","prima","seconda"])
    #a = str.find(st.session_state.mail,"@")
    #filename = st.session_state.mail[:a-1] + "PROVA.csv"
    
    A["mail"]=[st.session_state.mail]
    A["consenso"]=[st.session_state.consenso]
    A["prima"]=[st.session_state.prima]
    A["seconda"]=[st.session_state.seconda]

    st.write(A)
    #A.to_csv(filename)
    sh = gc.open('FOLLIE')
    wks = sh[0]
    column_count = find_empty_cell(wks)
    st.write(column_count)
    if column_count==1:
        wks.set_dataframe(A,(column_count,1))
    else:

        wks.set_dataframe(A,(column_count,1),copy_head=False)
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
