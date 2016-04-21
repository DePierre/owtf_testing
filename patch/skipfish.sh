#!/bin/sh
wget https://skipfish.googlecode.com/files/skipfish-2.10b.tgz
tar zxvf skipfish-2.10b.tgz
sudo apt-get install libidn11-dev
cd skipfish-2.10b
make
sudo rm -rf /usr/share/skipfish/*
sudo cp -rf ./assets /usr/share/skipfish/
sudo cp -rf ./dictionaries /usr/share/skipfish/
sudo cp -rf ./signatures /usr/share/skipfish/
sudo rm /usr/bin/skipfish
sudo cp -f ./skipfish /usr/bin/
