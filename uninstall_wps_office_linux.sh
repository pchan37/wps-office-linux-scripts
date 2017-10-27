#!/bin/bash -e

echo 'Removing WPS Office...'
sudo apt remove wps-office
sudo apt autoremove

echo 'Removing symbols required for WPS Office...'
sudo rm -rf /usr/share/fonts/wps-fonts
echo 'Rebuilding font cache...'
fc-cache -fvs

if command -v plank; then
    echo 'Removing the launchers for WPS Office from plank...'
    rm -rf ~/.config/wps-pchan-plank
fi

echo 'Successfully removed WPS Office!'
