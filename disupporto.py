import streamlit as st

a = st.radio("Quale è il tuo genere preferito?",('Comedy', 'Drama', 'Documentary'), key="prima")

a

st.session_state["prima"]