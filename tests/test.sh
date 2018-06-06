#!/bin/bash
set -e
DIR=$(dirname "$0")

PYTHON="python$PYVERSION -m coverage run -a --source $DIR/../src/"
$PYTHON $DIR/../src/dcm2hdr.py
$PYTHON $DIR/../src/dcm2hdr.py -h

#
# Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
# The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
# Dean Vaughan, http://deanvaughan.org/
#

# expected failed tests
$PYTHON $DIR/../src/dcm2hdr.py x && false || true
$PYTHON $DIR/../src/dcm2hdr.py x x && false || true
$PYTHON $DIR/../src/dcm2hdr.py x x x && false || true
$PYTHON $DIR/../src/dcm2hdr.py https://google.com x && false || true

wget -c -i ${DIR}/example_dicom_files.url -nv

for file in *dcm; do
  echo $file
  output=${file/dcm/png}
  echo "Convert: $output to PNG"
  $PYTHON $DIR/../src/dcm2hdr.py $file $output
  output=${file/dcm/tiff}
  echo "Convert: output to TIFF"
  $PYTHON $DIR/../src/dcm2hdr.py $file $output -z 0
  $PYTHON $DIR/../src/dcm2hdr.py $file $output -z 1
  $PYTHON $DIR/../src/dcm2hdr.py $file $output -z 2
  echo "$output is done."
done

$PYTHON $DIR/../src/dcm2hdr.py $file invalid.jpg && false || true
$PYTHON $DIR/../src/dcm2hdr.py $DIR/../src/dcm2hdr.py invalid.jpg && false || true

$PYTHON $DIR/../src/dcm2hdr.py $file $output  -z 0  -r 0.5
$PYTHON $DIR/../src/dcm2hdr.py $file $output -R -m -1000 -M 2000 -z 1
$PYTHON $DIR/../src/dcm2hdr.py $file $output -R -S -r 0.3 --offset -1000 -z 2
$PYTHON $DIR/../src/dcm2hdr.py $file $output  -s

rm -f *.png *.tiff *.dcm
echo
echo
echo "  TESTS ARE OK!  "