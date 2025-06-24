# Personalizados Vann SaaS

Sistema completo de gestão e produção de personalizados para pequenas gráficas, com foco total na experiência do cliente e produtividade operacional.

## 🚀 Módulos disponíveis

- 📂 **Catálogo de Modelos**: cadastro e gerenciamento de temas e modelos de arte.
- 🎨 **Personalizador**: inserção automática de nome e idade nas artes.
- 🏷️ **Produção**: upload, redimensionamento e organização dos pedidos prontos para impressão.

## 📦 Estrutura do Projeto

```
Personalizados-Vann-SaaS-Limpo
│
├── comerciais
│   ├── catalogo_modelos.py
│   └── personalizacao.py
│
├── producao
│   └── personalizados_vann_upload.py
│
├── utils
│   ├── ajuste_automatico.py
│   └── ocr_extrator.py
│
├── processador_imagem.py
├── registrador_pedidos.py
├── modelos
├── produzidos
├── uploads
├── venv
├── requirements.txt
└── main.py
```

## ⚙️ Instalação e execução

### 1️⃣ Clone o repositório (ou copie sua estrutura local)

### 2️⃣ Crie e ative o ambiente virtual

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o sistema

```bash
streamlit run main.py
```

## 🎯 Pronto para SaaS real!

A partir dessa base podemos evoluir para:
- Histórico de pedidos
- Controle de aprovação online
- Dashboard de produção
- Gestão multiusuário
- Backup e versionamento

---

Desenvolvido com ❤️ no Vann SaaS Project.
