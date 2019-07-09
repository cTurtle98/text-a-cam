# 
# SETUP script for text-a-cam project
#
# https://github.com/cTurtle98/text-a-cam
#

echo "this script automates raspi-config and sets up a pi for running this software and this software only"

echo "press any key to continue"
read

sudo raspi-config nonint do_expand_rootfs

locale=en_US.UTF-8
layout=us
sudo raspi-config nonint do_change_locale $locale
sudo raspi-config nonint do_configure_keyboard $layout

sudo raspi-config nonint do_camera 1

sudo raspi-config nonint do_ssh 1

sudo raspi-config nonint do_serial 1

#more raspi-config automation here

sudo apt install python3 python3-pip

