#!/bin/bash
set -e

PYTHON="python -m coverage run -a --source ../src"
$PYTHON ../src/dcm2hdr.py
$PYTHON ../src/dcm2hdr.py -h

#
# Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
# The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
# Dean Vaughan, http://deanvaughan.org/
#

wget -c -i example_dicom_files.url -nv

for file in *dcm; do
    echo $file
    output=${file/dcm/png}
    echo "Convert: $output to PNG"
    $PYTHON ../src/dcm2hdr.py $file $output
    output=${file/dcm/tiff}
    echo "Convert: output to TIFF"
    $PYTHON ../src/dcm2hdr.py $file $output
    echo "$output is done."
done
rm -f *.png *.tiff *.dcm
