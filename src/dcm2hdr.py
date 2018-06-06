#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np
import pydicom as dicom
import imageio
from contracts import contract
from optparse import OptionParser
import tifffile as tiff
import sys
import os

__version__ = '1.0.2'
__title__ = 'dcm2hdr'
__summary__ = 'DICOM to 16bit PNG/TIFF converter'
__uri__ = 'https://github.com/dvolgyes/dcm2hdr'
__license__ = 'AGPL v3'
__author__ = 'David Völgyes'
__email__ = 'david.volgyes@ieee.org'
__doi__ = '10.5281/zenodo.1246724'
__description__ = """
This program is meant to convert DICOM files to 16bit PNG or TIFF files.
The primary goal is to make images stored in DICOM files processable
with regular image processing tools, especially for tone mapping
which is not supported by regular DICOM viewers."""

__bibtex__ = """@misc{david_volgyes_2018_1246724,
  author  = {David Völgyes},
  title   = {DCM2HDR: DICOM to HDR image conversion.},
  month   = may,
  year    = 2018,
  doi     = {"""+__doi__+"""},
  url     = {https://doi.org/"""+__doi__+"""}
}"""

__reference__ = """David Völgyes. (2018, June 6).
DCM2HDR: DICOM to HDR image conversion (Version v"""+__version__+""").
Zenodo. https://doi.org/""" + __doi__


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def read_dicom(dcmfile, options):
    dcm = dicom.read_file(dcmfile, force=True)
    try:
        dcm.decompress()
        data = dcm.pixel_array
    except AttributeError:
        eprint('DICOM file seems to be incorrect, but try it anyway.')
        dcm.file_meta.TransferSyntaxUID = dicom.uid.ImplicitVRLittleEndian
        dcm.decompress()
        data = dcm.pixel_array
    try:
        a = dcm.RescaleSlope
    except AttributeError:
        a = 1
    try:
        b = dcm.RescaleIntercept
    except AttributeError:
        b = 0

    if options.offset is not None:
        b = options.offset
    if options.rescale is not None:
        a = options.rescale
        options.slope = True

    if options.raw or (a == 1 and b == 0):
        pass
    else:
        data = np.clip(data, options.min - b, options.max - b)
        if options.slope:
            data = data.astype(np.float) * a
            eprint('Warning: PNG and TIFF cannot handle floats! '
                   ' You will lose precision with rounding!')
    return data


@contract(img='array[NxMx...](uint8|uint16)')
def save_hdr(filename, img, dimension=None):
    dims = len(img.shape)
    if not (1 < dims <= 3):
        eprint('Unsupported number of dimensions')
        sys.exit(1)

    if dims == 3:
        name, ext = os.path.splitext(filename)
        if dimension is None:
            # smallest:
            if min(img.shape) < 20:
                dimension = np.argmin(img.shape)
            # if NxNxM -> M
            elif img.shape[0] == img.shape[1]:
                dimension = 2
            # if NxMxM -> N
            elif img.shape[1] == img.shape[2]:
                dimension = 0
            # if nothing works, use default 0
            else:
                dimension = 0

        for i in range(img.shape[dimension]):
            fname = '{}_{}{}'.format(name, i, ext)
            if dimension == 0:
                save_hdr(fname, img[i, ...])
            if dimension == 1:
                save_hdr(fname, img[:, i, :])
            if dimension == 2:
                save_hdr(fname, img[..., i])
    else:
        if filename.endswith('.png'):
            imageio.imsave(filename, img)
        elif filename.endswith('.tiff'):
            arr = np.dstack((img, img, img))
            tiff.imsave(filename, arr)
        else:
            eprint('Unsupported file format!')
            sys.exit(1)


if __name__ == '__main__':

    usage = ('usage: %prog [options] DCM_INPUT PNG/TIFF_OUTPUT')
    parser = OptionParser(usage=usage,
                          description=__description__,
                          prog=__title__,
                          version='%prog ' + __version__)

    parser.add_option('-c', '--cite',
                      dest='cite',
                      action='store_true',
                      default=False,
                      help='print citation information')

    parser.add_option('-R', '--raw',
                      dest='raw',
                      action='store_true',
                      default=False,
                      help='unprocessed raw pixeldata (default:false)')

    parser.add_option('-m', '--min',
                      dest='min',
                      action='store',
                      type='float',
                      default=-1024,
                      help='minimum allowed value (default:-1024)')

    parser.add_option('-M', '--max',
                      dest='max',
                      action='store',
                      type='float',
                      default=64511,
                      help='maximum allowed value (default:64511)')

    parser.add_option('-o', '--offset',
                      dest='offset',
                      action='store',
                      type='float',
                      default=None,
                      help='override default offset (default: use no offset)')

    parser.add_option('-r', '--rescale',
                      dest='rescale',
                      action='store',
                      type='float',
                      default=None,
                      help='override default rescale (default: 1)')

    parser.add_option('-S', '--enable-slope',
                      dest='slope',
                      action='store_true',
                      default=False,
                      help='enable rescale slope (default:false)')

    parser.add_option('-s', '--disable-slope',
                      dest='slope',
                      action='store_false',
                      default=False,
                      help='disable rescale slope (default: disable)')

    parser.add_option('-z', '--z-dimension',
                      dest='dimension',
                      action='store',
                      type='int',
                      default=None,
                      help='which dimension should be used'
                           'for slicing (3D) (default:auto detect)')

    (options, args) = parser.parse_args()

    if options.cite:
        print('Reference for this software:')
        print(__reference__)
        print()
        print('Bibtex format:')
        print(__bibtex__)
        sys.exit(0)

    if len(args) == 0:
        parser.print_help()
        sys.exit(0)

    if len(args) != 2:
        eprint('Exactly two input files are needed: HDR and LDR.')
        sys.exit(1)

    data = read_dicom(args[0], options)
    save_hdr(args[1], data.astype(np.uint16), options.dimension)
