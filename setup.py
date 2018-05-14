#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.util import get_platform


short_description = 'DCM2HDR - DICOM to HDR (16bit TIFF/PNG) converter'

with open('requirements.txt', 'rt') as f:
    reqs = list(map(str.strip, f.readlines()))

setup(
    name='dcm2hdr',
    version='1.0.1',
    description=short_description,
    long_description=short_description,
    author='David Volgyes',
    author_email='david.volgyes@ieee.org',
    url='https://github.com/dvolgyes/dcm2hdr',
    packages=['dcm2hdr'],
    package_dir={'dcm2hdr': 'src'},
    scripts=['src/dcm2hdr.py'],
    data_files=[],
    keywords=['DICOM', 'HDR', 'TIFF', 'PNG'],
    classifiers=[],
    license='AGPL3',
    platforms=[get_platform()],
    require=reqs,
    download_url='https://github.com/dvolgyes/dcm2hdr/archive/latest.tar.gz',
)
