import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import processador_imagem

# Novo módulo: Personalização
st.set_page_config(page_title="Personalização - Vann SaaS", page_icon="🎨", layout="centered")
st.title("🎨 Personalizador de Artes - Personalizados Vann SaaS")

# Diretório onde estão os temas e modelos cadastrados
PASTA_MODELOS = "modelos"
os.makedirs(PASTA_MODELOS, exist_ok=True)

# Seleção de tema
st.header("🎯 Selecione o Tema e o Modelo")
temas = os.listdir(PASTA_MODELOS)

if temas:
    tema_selecionado = st.selectbox("Escolha o tema:", temas)
    pasta_tema = os.path.join(PASTA_MODELOS, tema_selecionado)
    arquivos_disponiveis = [f for f in os.listdir(pasta_tema) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if arquivos_disponiveis:
        arquivo_base = st.selectbox("Selecione o arquivo base para personalizar:", arquivos_disponiveis)
        caminho_arquivo = os.path.join(pasta_tema, arquivo_base)

        # Coleta dos dados de personalização
        st.header("✍️ Informações de Personalização")
        nome = st.text_input("Nome da criança:")
        idade = st.text_input("Idade:")
        fonte_tamanho = st.slider("Tamanho da fonte:", 20, 150, 60)

        if st.button("Gerar Personalização"):
            if not nome or not idade:
                st.warning("Por favor, informe o nome e idade.")
            else:
                # Processa a imagem
                imagem = Image.open(caminho_arquivo).convert("RGBA")
                draw = ImageDraw.Draw(imagem)

                # Define posição aproximada (centro da imagem)
                largura, altura = imagem.size
                posicao_texto = (largura // 2, altura - (altura // 4))

                # Fonte (usando fonte padrão do sistema)
                try:
                    fonte = ImageFont.truetype("arial.ttf", fonte_tamanho)
                except:
                    fonte = ImageFont.load_default()

                texto = f"{nome} - {idade} anos"
                texto_largura, texto_altura = draw.textsize(texto, font=fonte)
                posicao_texto = ( (largura - texto_largura) // 2, (altura - texto_altura) - 50)

                draw.text(posicao_texto, texto, font=fonte, fill=(255, 0, 0, 255))

                # Exibe o preview
                st.subheader("🖼️ Preview da Personalização:")
                st.image(imagem, use_column_width=True)

                # Permite download
                buffer = io.BytesIO()
                imagem.save(buffer, format="PNG")
                buffer.seek(0)

                st.download_button(
                    label="📥 Baixar Arte Personalizada",
                    data=buffer,
                    file_name=f"{tema_selecionado}_{nome}_{idade}.png",
                    mime="image/png"
                )
    else:
        st.info("Este tema ainda não possui arquivos de imagem disponíveis para personalização.")
else:
    st.info("Nenhum tema cadastrado ainda.")
