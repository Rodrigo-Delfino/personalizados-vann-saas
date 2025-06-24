from PIL import Image
import os

# Tamanhos em pixels (exemplo: 300 DPI convertido de cm para px)
TAMANHOS = {
    "10x15": (1181, 1772),   # 10x15 cm
    "15x21": (1772, 2480),   # 15x21 cm
    "20x30": (2362, 3543)    # 20x30 cm
}

def processar_imagem(uploaded_file, tamanho):
    img = Image.open(uploaded_file)
    img = img.convert("RGB")

    largura, altura = TAMANHOS[tamanho]

    # Ajusta mantendo proporção (corte central se necessário)
    img.thumbnail((largura, altura), Image.LANCZOS)

    # Cria uma imagem branca no tamanho exato e centraliza
    fundo = Image.new("RGB", (largura, altura), (255, 255, 255))
    x_offset = (largura - img.width) // 2
    y_offset = (altura - img.height) // 2
    fundo.paste(img, (x_offset, y_offset))

    return fundo

def salvar_imagens(imagens, pedido, tamanho):
    pasta_destino = os.path.join("produzidos", pedido)
    os.makedirs(pasta_destino, exist_ok=True)

    for idx, uploaded_file in enumerate(imagens, start=1):
        imagem_tratada = processar_imagem(uploaded_file, tamanho)
        nome_arquivo = f"{pedido}_{idx}.jpg"
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        imagem_tratada.save(caminho_completo, "JPEG")
