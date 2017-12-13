#!/bin/bash

# run this script via: bash run.sh

# run the unit tests
nosetests --with-coverage test_get_data.py test_clean_data.py
# run the PEP8 checker
pycodestyle test_get_data.py test_clean_data.py

cd ..\

pycodestyle get_data.py clean_data.py
