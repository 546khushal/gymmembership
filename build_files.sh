#!/bin/bash
echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"

mkdir -p staticfiles_build
cp -r static/* staticfiles_build/