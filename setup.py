#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

short_description = 'DCM2HDR - DICOM to HDR (16bit TIFF/PNG) converter'
long_description = """DCM2HDR - DICOM to HDR (16bit TIFF/PNG) converter
The aim is to make it easier editing files with regular photo editor tools,
e.g. for presentation. The PNG files are single channel grayscale files,
the TIFFs are RGB encoded gray files (all channels have the same value).
"""

setuptools.setup(
    name='dcm2hdr',
    version='1.0.2',
    author='David Völgyes',
    author_email='david.volgyes@ieee.org',
    description=short_description,
    description_content_type='text/plain',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/dvolgyes/dcm2hdr',
    license='AGPL3',
    scripts=['src/dcm2hdr.py'],
    python_requires='>=2.7',
    setup_requires=[],
    install_requires=['numpy>=1.13.3,<2.0',
                      'pycontracts>=1.8.3,<2.0',
                      'imageio>=2.3.0,<3.0',
                      'tifffile>=0.14.0,<1.0'
                      'pydicom>=1.0,<2.0'
                      ],
    keywords=['DICOM', 'HDR', 'TIFF', 'PNG'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3',
    ),
)
