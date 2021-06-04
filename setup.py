#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(name='audiokit',
    version='0.0.1',
    description='Design and analyze speech, acoustic, and audio processing systems',
    author='wxqwinner',
    author_email='wxqwinner@gmail.com',
    url='https://github.com/wxqwinner/audiokit',
    python_requires='>=3.6',
    packages=find_packages(),
    long_description=open(os.path.join(here, 'README.md')).read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'],

    install_requires=[
          'pydub>=0.23.1',
          'numpy>=1.19.5',]
)

