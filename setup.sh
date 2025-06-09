#!/bin/sh
DEST=/usr/lib/enigma2/python/Plugins/Extensions/DB920PluginFetcher
rm -rf "$DEST"
mkdir -p "$DEST"
cp plugin.py feeds.py wordpress.py config.py __init__.py "$DEST/"
cp requirements.txt "$DEST/"
echo "Installing dependencies..."
opkg update
opkg install python3-feedparser python3-requests
echo "Done. Restarting enigma2."
killall enigma2
