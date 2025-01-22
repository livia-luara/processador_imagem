from setuptools import setup, find_packages

setup(
    name='processador_img',  
    version='0.1.0',  
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'pillow'],  
    description='Pacote para processamento de imagens',
    author='Lívia Luara',
    author_email='livialosc@gmail.com',
    url='https://github.com/livia-luara/processador_imagem',  
    python_requires='>=3.6',  
)
