import numpy as np
import cv2
import easyocr
from utils import ajuste_automatico, ocr_extrator
from PIL import Image

def processar_imagem(uploaded_file):
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    
    # Pré-processamento
    imagem_corrigida = ajuste_automatico.ajustar_imagem(image_np)

    # OCR
    textos_detectados = ocr_extrator.extrair_texto(imagem_corrigida)

    # Converte imagem processada para exibição no Streamlit
    imagem_final = Image.fromarray(imagem_corrigida)

    return imagem_final, textos_detectados


