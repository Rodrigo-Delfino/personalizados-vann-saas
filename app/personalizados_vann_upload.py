import streamlit as st
import os
from processador_imagem import salvar_imagens

# Configurações da página
st.set_page_config(page_title="Personalizados Vann SaaS - Upload de Imagens", page_icon="🖼️")

st.title("Personalizados Vann SaaS - Upload de Imagens")

# Formulário
with st.form("formulario_upload", clear_on_submit=False):
    nome_pedido = st.text_input("Nome do pedido:")
    observacoes = st.text_area("Observações (opcional):")
    tamanho_impressao = st.selectbox("Selecione o tamanho de impressão:", ["10x15", "15x21", "20x30"])
    imagens = st.file_uploader("Selecione as imagens", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    enviar = st.form_submit_button("Enviar")

# Processamento
if enviar:
    if not nome_pedido:
        st.warning("Por favor, preencha o nome do pedido.")
    elif not imagens:
        st.warning("Por favor, selecione pelo menos uma imagem.")
    else:
        pasta = salvar_imagens(imagens, nome_pedido, tamanho_impressao)
        st.success(f"Imagens salvas em: `{pasta}`")

