import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import processador_imagem

# Novo módulo: Cadastro de Modelos
st.set_page_config(page_title="Catálogo de Modelos - Vann SaaS", page_icon="📁", layout="centered")
st.title("📁 Catálogo de Modelos - Personalizados Vann SaaS")

# Define o diretório base dos modelos
PASTA_MODELOS = "modelos"
os.makedirs(PASTA_MODELOS, exist_ok=True)

# Formulário de cadastro de novo tema
st.header("📌 Cadastro de Novo Tema")
nome_tema = st.text_input("Nome do novo tema:")
modelos_files = st.file_uploader("Faça o upload dos arquivos de modelo (arte base, moldes, imagens)", type=["png", "jpg", "jpeg", "pdf", "svg"], accept_multiple_files=True)

if st.button("Cadastrar Tema"):
    if not nome_tema or not modelos_files:
        st.warning("Por favor, informe o nome do tema e envie ao menos um arquivo.")
    else:
        pasta_tema = os.path.join(PASTA_MODELOS, nome_tema)
        os.makedirs(pasta_tema, exist_ok=True)
        
        for arquivo in modelos_files:
            caminho = os.path.join(pasta_tema, arquivo.name)
            with open(caminho, "wb") as f:
                f.write(arquivo.getbuffer())
        
        st.success(f"Tema '{nome_tema}' cadastrado com sucesso!")
        st.toast("Tema adicionado ao catálogo.")

# Lista de temas já cadastrados
st.header("🎯 Temas Cadastrados")
temas = os.listdir(PASTA_MODELOS)

if temas:
    tema_selecionado = st.selectbox("Selecione um tema para visualizar:", temas)
    arquivos_tema = os.listdir(os.path.join(PASTA_MODELOS, tema_selecionado))

    st.subheader(f"Arquivos do tema '{tema_selecionado}':")
    for arquivo in arquivos_tema:
        st.write(f"- {arquivo}")
else:
    st.info("Nenhum tema cadastrado ainda.")
