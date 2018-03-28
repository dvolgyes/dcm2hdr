REM #
REM # Test dicom files are downloaded from: http://deanvaughan.org/wordpress/2013/07/dicom-sample-images/
REM # The website is under Creative Commons 4.0 Attribution - Non-commercial license, so here is the credit:
REM # Dean Vaughan, http://deanvaughan.org/
REM #

REM # expected failed tests
dir
wget -c -i ${DIR}/example_dicom_files.url -nv

echo "  TESTS ARE OK!  "
