#!/bin/sh
wget https://skipfish.googlecode.com/files/skipfish-2.10b.tgz
tar zxvf skipfish-2.10b.tgz
sudo apt-get install libidn11-dev
cd skipfish-2.10b
sudo make
