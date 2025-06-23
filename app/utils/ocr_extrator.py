import easyocr

def extrair_texto(imagem_np):
    reader = easyocr.Reader(['pt', 'en'])
    resultados = reader.readtext(imagem_np)
    textos = [res[1] for res in resultados]
    return textos
