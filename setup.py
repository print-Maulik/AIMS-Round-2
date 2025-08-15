from setuptools import setup, find_packages

setup(
    name='scene_localization',
    version='1.0.0',
    author='Maulik Rawat',
    author_email='your.email@example.com',
    description='Scene localization in dense images via natural language queries using ResNet50 and GloVe embeddings (TensorFlow).',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.0.0',
        'numpy',
        'Pillow',
        'nltk',
        'matplotlib'
    ],
    python_requires='>=3.8',
)
