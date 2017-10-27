#!/bin/bash -e

if command -v plank > /dev/null; then
    rm -rf ~/.wps
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
