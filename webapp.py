import streamlit as st
st.header('Sasi GM')
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
 st.chat_input("Say something")
