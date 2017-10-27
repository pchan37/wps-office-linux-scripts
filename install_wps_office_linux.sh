#!/bin/bash -e

echo 'WPS Office installation script brought to you by PChan!'

echo 'Downloading WPS Office!'
wget -q http://kdl1.cache.wps.com/ksodl/download/linux/a21//wps-office_10.1.0.5707~a21_amd64.deb

echo 'Downloading the symbols for WPS Office!'
wget -q https://github.com/IamDH4/ttf-wps-fonts/archive/master.zip

echo 'Installing WPS Office!'
sudo dpkg -i wps-office_10.1.0.5707~a21_amd64.deb
rm wps-office_10.1.0.5707~a21_amd64.deb

echo 'Installing the symbols for WPS Office!'
unzip master.zip
cd ttf-wps-fonts-master && sudo bash install.sh
cd ..
rm -rf ttf-wps-fonts-master
rm master.zip

if command -v plank > /dev/null; then

    read -r -p "Do you want to install the launchers for the dock? [Y/N] " response
    if [[ "$response" =- ^([yY][eE][sS]|[yY])+$ ]]
    then            #
        rm -rf ~/wps
        mkdir -p ~/wps

        cp /usr/share/applications/wps-office-et.desktop ~/wps/
        cp /usr/share/applications/wps-office-wpp.desktop ~/wps/
        cp /usr/share/applications/wps-office-wps.desktop ~/wps/

        chmod a+x ~/wps/*

        DOCKITEM_FILE_CONTENT='[PlankDockItemPreferences]\nLauncher=file:///home/<username>/wps'
        TAILORED_DOCKITEM_FILE_CONTENT="${DOCKITEM_FILE_CONTENT/<username>/$(whoami)}"

        echo -en $TAILORED_DOCKITEM_FILE_CONTENT > ~/.config/plank/dock1/launchers/wps.dockitem

        echo 'Success!'
    fi

echo 'Done!'
