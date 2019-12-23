DCM2HDR: DICOM to HDR converter
===============================
Travis:[![Build Status](https://travis-ci.org/dvolgyes/dcm2hdr.svg?branch=master)](https://travis-ci.org/dvolgyes/dcm2hdr)
Semaphore:[![Build Status](https://semaphoreci.com/api/v1/dvolgyes/dcm2hdr/branches/master/badge.svg)](https://semaphoreci.com/dvolgyes/dcm2hdr)
CircleCI:[![Build status](https://circleci.com/gh/dvolgyes/dcm2hdr.svg?style=svg)](https://circleci.com/gh/dvolgyes/dcm2hdr)
AppVeyor:[![Build status](https://ci.appveyor.com/api/projects/status/fcxff46jgyj32tgo?svg=true)](https://ci.appveyor.com/project/dvolgyes/dcm2hdr)

Coveralls:[![Coverage Status](https://coveralls.io/repos/github/dvolgyes/dcm2hdr/badge.svg?branch=master)](https://coveralls.io/github/dvolgyes/dcm2hdr?branch=master)
Codecov:[![codecov](https://codecov.io/gh/dvolgyes/dcm2hdr/branch/master/graph/badge.svg)](https://codecov.io/gh/dvolgyes/dcm2hdr)
Snyk:[![Known Vulnerabilities](https://snyk.io/test/github/dvolgyes/dcm2hdr/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dvolgyes/dcm2hdr?targetFile=requirements.txt)


[![pyversion](https://img.shields.io/pypi/pyversions/dcm2hdr.svg)](https://pypi.org/project/dcm2hdr/)
[![PyPI - License](https://img.shields.io/pypi/l/dcm2hdr.svg)](https://gitlab.com/dvolgyes/dcm2hdr/raw/master/LICENSE.txt)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1246664.svg)](https://doi.org/10.5281/zenodo.1246664)

This is a Python3 converter tool which converts DICOM files to 16 bit PNG and TIFF files.
The aim is to make it easier editing files with regular photo editor tools, e.g. for presentation.
The PNG files are single channel grayscale files, 
the TIFFs are RGB encoded gray files (all channels have the same value).

Technically, there are several file formats for high bit depth images, e.g. Radiance HDR, OpenEXR, etc.
However, 16bit seems to be enough, and these formats are more complicated than TIFF/PNG.
If you need Radiance HDR/OpenEXR, and 16bit png is not enough, then open a ticket, and let me know.

The software is kind of trivial, you don't have to cite it, but if you want, then you could use DOI shield above,
or query the latest reference from command line:
```
dcm2hdr.py --cite
```
The query will provide both plain text and BiBTeX information.

Source code
-----------

The code is hosted at Github and GitLab too, with the exact same content.
However, on long term, the project will migrate to GitLab, so please, use the GitLab site:
[https://gitlab.com/dvolgyes/dcm2hdr](https://gitlab.com/dvolgyes/dcm2hdr)



Install
-------

```
pip install dcm2hdr
```
or directly from the git repository:
```
pip install git+https://gitlab.com/dvolgyes/dcm2hdr
```

Afterwards, you can query the command line options:
```
dcm2hdr -h
```

but the default settings should work for most use cases:
```
dcm2hdr.py DICOM_INPUT_FILE  PNG_or_TIFF_OUTPUT
```

URLs: I plan to add support to open dicom files directly from internet,
but I do not guarantee this to work. Also, I rely on the dicom 
package from PyPi. If the DICOM format is not supported by this library,
then I cannot do anything. (It is rare, but some scanner use compressed
dicoms, encryption, etc. DCMTK/GDCM can handle most of the weird issues,
so if you need to process such files, use DCMTK or GDCM to convert
the source files to something more standard.)

Documentation
-------------
The tool itself is simple, the help message is reasonable:

```
dcm2hdr.py -h
```

but if you need more, open a github ticket and explain what is missing.

Issues
------
If you discover any issues, please open a ticket on Github.