# protocol_port/setup.py

from setuptools import setup, find_packages

setup(
    name='protocol_port',
    version='0.1',
    packages=find_packages(),
    description='Un package pour obtenir le port d\'un protocole donné',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Amine elarouji',
    author_email='amineelarouji@gmail.com',
    url='https://protocol.com/protocol-port',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
