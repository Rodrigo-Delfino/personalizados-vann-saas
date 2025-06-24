# Personalizados Vann SaaS - Cloud Version

Sistema SaaS para gestão de personalizados, agora estruturado no formato oficial de Multi-Page do Streamlit Cloud.

---

## 🚀 Estrutura do Projeto

```
Personalizados-Vann-SaaS-Cloud
│
├── pages
│   ├── 1_Catalogo_Modelos.py
│   ├── 2_Personalizador.py
│   └── 3_Producao.py
│
├── utils
│   ├── ajuste_automatico.py
│   └── ocr_extrator.py
│
├── processador_imagem.py
├── registrador_pedidos.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Como rodar localmente

1️⃣ Crie o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  (Windows)
# ou
source venv/bin/activate  (Linux/Mac)
```

2️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

3️⃣ Rode o Streamlit:

```bash
streamlit run pages/1_Catalogo_Modelos.py
```

---

## ☁️ Como rodar no Streamlit Cloud

- Faça o deploy direto conectando o repositório GitHub.
- O Streamlit Cloud detecta a pasta `pages/` automaticamente e cria o menu.
- Não há necessidade de configurar Python Path ou fazer ajustes de imports.

---

## 📦 requirements.txt

```
streamlit==1.35.0
Pillow==10.3.0
```

---

## 🚀 Pronto para escalar SaaS Vann 2.0

- Histórico de pedidos
- Aprovação online
- Dashboard de produção
- Controle multiusuário
- Backup e monitoramento

---

Desenvolvido com ❤️ por Rodrigo e Buddy (ChatGPT).
