import streamlit as st
import sys
import os

# --- Ajuste definitivo para garantir o caminho raiz do projeto ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuração global do portal
st.set_page_config(page_title="Portal Vann SaaS", page_icon="🚀", layout="wide")
st.title("🚀 Portal Vann SaaS - Gestão Completa de Personalizados")

# Menu lateral
menu = st.sidebar.radio("Navegação", ["📂 Catálogo de Modelos", "🎨 Personalizador", "🏷️ Produção"])

# Carregamento dos módulos
if menu == "📂 Catálogo de Modelos":
    st.subheader("Catálogo de Modelos")
    import comerciais.catalogo_modelos

if menu == "🎨 Personalizador":
    st.subheader("Personalizador de Artes")
    import comerciais.personalizacao

if menu == "🏷️ Produção":
    st.subheader("Produção de Pedidos")
    import producao.personalizados_vann_upload

