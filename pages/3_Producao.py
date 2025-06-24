import streamlit as st
import os
import processador_imagem  # Ajuste o import conforme a sua estrutura de pacotes

# Configuração da página
st.set_page_config(page_title="Personalizados Vann SaaS", page_icon="🎨", layout="centered")
st.title("🎨 Personalizados Vann SaaS")
st.write("Organize, redimensione e prepare seus pedidos de forma simples.")

# Formulário
with st.form("formulario"):
    st.header("📦 Cadastro de Pedido")
    nome_pedido = st.text_input("Nome do Pedido:")
    tamanho_opcao = st.selectbox("Selecione o tamanho de impressão:", ("10x15", "15x21", "20x30"))
    observacoes = st.text_area("Observações:")
    imagens = st.file_uploader("Selecione as imagens", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    enviar = st.form_submit_button("Processar Pedido")

# Processamento
if enviar:
    if not nome_pedido or not imagens:
        st.warning("⚠️ Por favor, informe o nome do pedido e selecione pelo menos uma imagem.")
    else:
        with st.spinner("Processando imagens..."):
            pasta = processador_imagem.salvar_imagens(imagens, nome_pedido, tamanho_opcao, observacoes)
        
        st.success("✅ Pedido processado com sucesso!")
        st.toast(f"Pedido '{nome_pedido}' está pronto para impressão.")
        st.write(f"Arquivos salvos na pasta: `{pasta}`")
