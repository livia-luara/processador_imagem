from setuptools import setup, find_packages

setup(
    name='processador_img',  
    version='0.1.0',  
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'pillow'],  # Dependências do seu pacote
    description='Pacote para processamento de imagens',
    author='Lívia Luara',
    author_email='seuemail@exemplo.com',
    url='https://github.com/seuusuario/processador_img',  # Se disponível
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
