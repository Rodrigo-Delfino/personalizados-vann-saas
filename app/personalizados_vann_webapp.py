import streamlit as st
from pipeline_ia import processar_imagem

st.set_page_config(page_title="Personalizados Vann SaaS", layout="centered")
st.title("Personalizados Vann SaaS")

uploaded_file = st.file_uploader("Selecione uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Imagem Original", use_column_width=True)

    if st.button("Processar Imagem"):
        imagem_processada, textos_detectados = processar_imagem(uploaded_file)

        st.image(imagem_processada, caption="Imagem Processada", use_column_width=True)
        st.subheader("Textos Detectados")
        for texto in textos_detectados:
            st.write(f"- {texto}")

