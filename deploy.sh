#!/bin/bash

# Build the website html files
./compile.py

# Remove old website directory
sudo rm -rfv /var/www/html/Wiki

# Copy fresh build into webserver root
sudo cp -rv html/Wiki /var/www/html
