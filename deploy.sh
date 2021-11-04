#!/bin/bash
./compile.py
sudo bash -c "rm -rfv /var/www/html/Wiki && cp -rv html/Wiki /var/www/html"
