import streamlit as st
import os

st.set_page_config(page_title="Catálogo de Modelos - Vann SaaS", page_icon="📂", layout="wide")

# CSS para o botão verde bonito
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 16px;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center; color: #2196F3;'>📂 Catálogo de Modelos</h1>", unsafe_allow_html=True)
st.markdown("---")

# Diretório de armazenamento
diretorio_modelos = "modelos"
os.makedirs(diretorio_modelos, exist_ok=True)

# Formulário de cadastro
with st.form("form_cadastro_tema"):
    st.subheader("📌 Cadastro de Novo Tema")
    nome_tema = st.text_input("Nome do novo tema:")
    arquivos = st.file_uploader("Faça o upload dos arquivos de modelo (arte base, moldes, imagens)", accept_multiple_files=True, type=['png', 'jpg', 'jpeg', 'pdf', 'svg'])
    submit = st.form_submit_button("Cadastrar Tema")

    if submit and nome_tema:
        pasta_tema = os.path.join(diretorio_modelos, nome_tema)
        os.makedirs(pasta_tema, exist_ok=True)
        for arquivo in arquivos:
            with open(os.path.join(pasta_tema, arquivo.name), "wb") as f:
                f.write(arquivo.getbuffer())
        st.success(f"Tema '{nome_tema}' cadastrado com sucesso!")

st.markdown("---")

# Exibir temas cadastrados
st.subheader("🎯 Temas Cadastrados")
temas = os.listdir(diretorio_modelos)
if temas:
    for tema in temas:
        st.markdown(f"✅ **{tema}**")
else:
    st.info("Nenhum tema cadastrado ainda.")


