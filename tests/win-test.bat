REM #
REM # Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
REM # The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
REM # Dean Vaughan, http://deanvaughan.org/
REM #

REM # expected failed tests
cd tests
dir
wget -c -i example_dicom_files.url -nv
python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm -h
python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm --version
python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm        out.png
python ../src/dcm2hdr.py CT-MONO2-16-brain.dcm        out.tiff -R
python ../src/dcm2hdr.py xr_hands.dcm                 out.png  -m -1000
python ../src/dcm2hdr.py xr_skull.dcm                 out.tiff -M 1500
python ../src/dcm2hdr.py xr_tspine.dcm                out.png  -r 2 -S
python ../src/dcm2hdr.py xr_chest.dcm                 out.tiff -s 
python ../src/dcm2hdr.py MR-MONO2-8-16x-heart.dcm     out.png  -o 2000 
python ../src/dcm2hdr.py US-MONO2-8-8x-execho.dcm     out.tiff
python ../src/dcm2hdr.py US-RGB-8-epicard.dcm         out.png
python ../src/dcm2hdr.py US-RGB-8-esopecho.dcm        out.tiff
python ../src/dcm2hdr.py US-PAL-8-10x-echo.dcm        out.png

echo "  TESTS ARE OK!  "
