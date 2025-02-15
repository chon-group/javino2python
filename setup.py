from setuptools import setup, find_packages
import serial
import time

VERSION = '0.1.7'
DESCRIPTION = 'Python library of Javino'
LONG_DESCRIPTION = 'A serial message error check protocol for exchanging messages between high-end and low-end IoT devices over serial communication.'

# Setting up
setup(
    name="javino",
    version=VERSION,
    author="ChonGroup",
    author_email="<chon@grupo.cefet-rj.br>",
    description=DESCRIPTION,
    url='https://github.com/chon-group/javino2python',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyserial'],
    keywords=['python', 'serial', 'jason'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# how to compile the package?
# python3 setup.py sdist bdist_wheel
