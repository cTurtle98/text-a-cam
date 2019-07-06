# 
# SETUP script for text-a-cam project
#
# https://github.com/cTurtle98/text-a-cam
#

echo "this script automates raspi-config and sets up a pi for running this software and this software only"

echo "press any key to continue"
read

sudo raspi-config nonint do_expand_rootfs

#more raspi-config automation here

sudo apt install python3 python3-pip

