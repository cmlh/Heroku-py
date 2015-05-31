#!/bin/sh
pip install gunicorn
pip install bottle
# Windows
# pip freeze > .\requirements.txt
pip freeze > requirements.txt
