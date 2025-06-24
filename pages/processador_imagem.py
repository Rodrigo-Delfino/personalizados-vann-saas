import os
from PIL import Image

def salvar_imagens(imagens, pedido, tamanho, observacoes=None):
    pasta_destino = os.path.join("produzidos", pedido)
    os.makedirs(pasta_destino, exist_ok=True)

    # Salva observações (caso existam)
    if observacoes:
        with open(os.path.join(pasta_destino, "OBSERVACOES.txt"), "w", encoding="utf-8") as f:
            f.write(observacoes)

    for imagem in imagens:
        nome_arquivo = imagem.name
        caminho = os.path.join(pasta_destino, nome_arquivo)

        with open(caminho, "wb") as f:
            f.write(imagem.getbuffer())

        # Opcionalmente podemos adicionar aqui o redimensionamento da imagem conforme o tamanho escolhido
        redimensionar_imagem(caminho, tamanho)

    return pasta_destino

def redimensionar_imagem(caminho, tamanho):
    img = Image.open(caminho)

    # Simples conversão dos tamanhos para pixels
    tamanhos_pixels = {
        "10x15": (1000, 1500),
        "15x21": (1500, 2100),
        "20x30": (2000, 3000)
    }

    if tamanho in tamanhos_pixels:
        img = img.resize(tamanhos_pixels[tamanho], Image.Resampling.LANCZOS)
        img.save(caminho)

