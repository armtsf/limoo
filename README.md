# Limoo

Limoo shows lyrics for the current playing song in your browser.
Supports Spotify, VLC, Rhythmbox, Amarok, and others.

![limoo](static/limoo.png?raw=true)

### Install
You need python 2.6 or newer python 2.x and [python-pip](https://github.com/pypa/pip).

#### Ubuntu:
    wget https://github.com/acrisci/playerctl/releases/download/v0.5.0/playerctl-0.5.0_amd64.deb
    sudo apt-get install ./playerctl-0.5.0_amd64.deb
    sudo pip install -r requirements.txt

#### Arch Linux:
    yaourt -S playerctl-git
    sudo pip install -r requirements.txt

### Usage
    python2 run.py

and point your web browser to http://localhost:5000.