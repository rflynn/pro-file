rem -- pro-file build script for Windows


rem -- doc first
cd doc\
python from-to-mapping.py > from-to-mapping.html


rem -- then data
cd ..\data\
del /f names.sqlite3
python population-us.py | sqlite3 names.sqlite3
python life-table-us.py | sqlite3 names.sqlite3
python givenname-birthyear-us.py
python surname-origin.py
python surname-ethnicity-us.py


rem -- summarize
sqlite3 names.sqlite3 < givenname-gender-summary.sql

