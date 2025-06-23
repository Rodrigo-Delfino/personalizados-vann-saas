import cv2
import numpy as np

def ajustar_imagem(imagem_np):
    imagem_cinza = cv2.cvtColor(imagem_np, cv2.COLOR_RGB2GRAY)
    imagem_borrada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    _, imagem_thresh = cv2.threshold(imagem_borrada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    imagem_corrigida = cv2.cvtColor(imagem_thresh, cv2.COLOR_GRAY2RGB)
    return imagem_corrigida


