#!/bin/python3
import os

sudo_hasło = '' #hasło
komendy = [ "apt update", "apt upgrade -y", "apt dist-upgrade -y","apt-get clean", "apt-get autoremove" ]

for komenda in komendy:
    os.system(f'echo {sudo_hasło}|sudo -S {komenda}')

input()
