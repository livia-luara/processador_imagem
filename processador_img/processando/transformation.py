# transformation.py

import numpy as np
from PIL import Image

def dominant_color(image):
    """
    Retorna a cor predominante da imagem em formato RGB.
    A cor predominante é obtida pela média dos valores de RGB.
    """
    # Converte a imagem e calcula a média para cada canal
    image_array = np.array(image)
    r, g, b = np.mean(image_array, axis=(0, 1))
    return int(r), int(g), int(b)

def apply_color_transformation(image, target_color):
    """
    Aplica uma transformação de cor na imagem, alterando a cor predominante
    para a cor alvo (target_color).
    """
    image_array = np.array(image)

    # Determina o fator de alteração para cada canal (R, G, B)
    target_r, target_g, target_b = target_color
    image_r, image_g, image_b = np.mean(image_array, axis=(0, 1))

    # Calcula o fator de escala para cada canal de cor
    scale_r = target_r / image_r if image_r != 0 else 1
    scale_g = target_g / image_g if image_g != 0 else 1
    scale_b = target_b / image_b if image_b != 0 else 1

    # Aplica o ajuste de cor em cada canal
    transformed_image = image_array.copy()
    transformed_image[:, :, 0] = np.clip(transformed_image[:, :, 0] * scale_r, 0, 255)  # Red
    transformed_image[:, :, 1] = np.clip(transformed_image[:, :, 1] * scale_g, 0, 255)  # Green
    transformed_image[:, :, 2] = np.clip(transformed_image[:, :, 2] * scale_b, 0, 255)  # Blue

    return Image.fromarray(transformed_image.astype(np.uint8))

def transform_image_by_color(image, reference_image):
    """
    Aplica a cor predominante da referência na imagem original.
    A imagem de referência (por exemplo, roxa) determinará a nova tonalidade da imagem original (por exemplo, verde).
    """
    # Determina a cor predominante da imagem de referência 
    target_color = dominant_color(reference_image)
    
    # Aplica a transformação de cor na imagem original
    transformed_image = apply_color_transformation(image, target_color)
    
    return transformed_image
