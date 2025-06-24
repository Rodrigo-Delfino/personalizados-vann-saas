import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal Vann SaaS", page_icon="🎨", layout="wide")

# Título principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎨 Portal Vann SaaS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555555;'>Personalizados com Estilo e Produtividade</h3>", unsafe_allow_html=True)
st.markdown("---")

# Layout de cards com alinhamento central
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:30px;border-radius:15px;box-shadow: 2px 2px 8px grey; text-align:center'>
        <h3>📂 Catálogo de Modelos</h3>
        <p>Gerencie seus modelos e temas prontos para produção.</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("👉 Ir para Catálogo", key="catalogo"):
        st.switch_page("pages/1_Catalogo_Modelos.py")

with col2:
    st.markdown("""
    <div style='background-color:#FFF3E0;padding:30px;border-radius:15px;box-shadow: 2px 2px 8px grey; text-align:center'>
        <h3>🎯 Personalizador</h3>
        <p>Personalize nomes, idades e detalhes dos seus pedidos.</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("👉 Ir para Personalizador", key="personalizador"):
        st.switch_page("pages/2_Personalizador.py")

with col3:
    st.markdown("""
    <div style='background-color:#E8F5E9;padding:30px;border-radius:15px;box-shadow: 2px 2px 8px grey; text-align:center'>
        <h3>🏷️ Produção</h3>
        <p>Envie imagens, redimensione e organize os arquivos prontos para imprimir.</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("👉 Ir para Produção", key="producao"):
        st.switch_page("pages/3_Producao.py")

st.markdown("---")
st.success("Vann SaaS 2.0 com interface centralizada e organizada!")

