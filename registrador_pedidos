import csv
import os
from datetime import datetime

ARQUIVO_PEDIDOS = "pedidos.csv"

def registrar_pedido(pedido, tamanho, quantidade, observacoes):
    novo = not os.path.exists(ARQUIVO_PEDIDOS)

    with open(ARQUIVO_PEDIDOS, mode='a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        if novo:
            writer.writerow(["DataHora", "Pedido", "Tamanho", "Qtd_Imagens", "Observações"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pedido,
            tamanho,
            quantidade,
            observacoes
        ])
