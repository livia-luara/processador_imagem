from PIL import Image

def load_image(filepath):
    """
    Carrega uma imagem do arquivo especificado.
    """
    return Image.open(filepath)

def save_image(image, filepath):
    """
    Salva a imagem no caminho especificado.
    """
    image.save(filepath)

def save_as_png(image, filepath):
    """
    Salva a imagem como um PNG.
    """
    image.save(filepath, "PNG")
