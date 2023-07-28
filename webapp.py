import streamlit as st
import numpy as np
st.header('Sasi Chatter Box')
with st.chat_message("user"):
    st.write("Hello Which Animal do you like 👋")
    #st.line_chart(np.random.randn(30, 3))

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

# Display a chat input widget.
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
