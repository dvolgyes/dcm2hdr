#!/bin/bash
set -e
#
# Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
# The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
# Dean Vaughan, http://deanvaughan.org/
#

wget -c -i example_dicom_files.url -nv

for file in *dcm; do
    echo $file
    output=${file/dcm/png}
    python ../src/dcm2hdr.py $file $output
    output=${file/dcm/tiff}
    ../src/dcm2hdr.py $file $output
done
rm -f *.png *.tiff *.dcm
