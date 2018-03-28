REM #
REM # Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
REM # The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
REM # Dean Vaughan, http://deanvaughan.org/
REM #

REM # expected failed tests
cd tests
wget -c -i example_dicom_files.url -nv
if %errorlevel% neq 0 exit /b %errorlevel%

python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm -h
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm --version
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py CT-MONO2-16-ankle.dcm        out1.png
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py CT-MONO2-16-brain.dcm        out2.tiff -R
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py xr_hands.dcm                 out3.png  -m -1000
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py xr_skull.dcm                 out4.tiff -M 1500
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py xr_tspine.dcm                out5.png  -r 2 -S
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py xr_chest.dcm                 out6.tiff -s 
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py MR-MONO2-8-16x-heart.dcm     out7.png  -o 2000 
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py US-MONO2-8-8x-execho.dcm     out8.tiff
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py US-RGB-8-epicard.dcm         out9.png
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py US-RGB-8-esopecho.dcm        out10.tiff
if %errorlevel% neq 0 exit /b %errorlevel%
python ../src/dcm2hdr.py US-PAL-8-10x-echo.dcm        out11.png
if %errorlevel% neq 0 exit /b %errorlevel%

dir
