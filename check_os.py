#!/bin/python3
import distro
import sys
import urllib.request
import json
import re

#insert the url of your web server as well as the path of your file
url = 'https://your_http_server/os-version.json'

if distro.id() == 'debian':
    with urllib.request.urlopen(url) as os_vers:
        data = json.loads(os_vers.read().decode('utf-8'))
    with open('/etc/debian_version') as deb:
        debian_version = deb.read().strip()
        split_release = debian_version.split(".",1)
        current_release = split_release[0]
        current_update = split_release[1]

        if int(current_release) < int(data['debian_old_stable']):
            print("Your Debian installation is very old. An upgrade is urgently needed.")
            sys.exit(2)
        elif int(current_release) < int(data['debian_major_release']):
            print("Your Debian (" + debian_version+ ") needs to switch to the last stable release. ")
            sys.exit(1)
        else:
            if int(current_update) < int(data['debian_last_major_update']):
                print("Your Debian version (" + debian_version+ ") is the last stable version but an upgrade is needed.")
                sys.exit(1)
            elif int(current_update) > int(data['debian_last_major_update']):
                print("Your Debian version (" + debian_version+ ") is more recent than expected in os-version file. Please update the os-version file.")
                sys.exit(1)
            else:
                print("Your Debian version (" + debian_version+ ") is the latest one and up to date. All OK")
                sys.exit(0)

elif distro.id() == 'centos' :
    with urllib.request.urlopen(url) as os_vers:
        data = json.load(os_vers)

        if int(data['centos_critical']) <= int(distro.version()) < int(data['centos_last']):
            print("Your CentOS version ("+ distro.version()+ ") is old. An upgrade is needed. ")
            sys.exit(1)
        else:
            if int(distro.version()) < int(data['centos_critical']):
                print("Your CentOS version ("+ distro.version()+ ") is very old. An upgrade is needed." )
                sys.exit(2)
            else:
                print("Your CentOS version ("+ distro.version()+ ") is the latest. All OK.")
                sys.exit(0)

elif distro.id() == 'ubuntu' :
    with urllib.request.urlopen(url) as os_vers:
        data = json.loads(os_vers.read().decode('utf-8'))
    with open('/etc/issue.net') as ubuntu:

        if 18.04 <= float(distro.version()) < float(data['ubuntu_major_release']) :
            print("Your Ubuntu version (" + ubuntu.read().strip()[7:-4]+ ") is old. An upgrade is needed. ")
            sys.exit(1)
        else:
            if float(distro.version()) < 18.04:
                print("Your Ubuntu version (" + ubuntu.read().strip()[7:-4]+ ") is very old. An upgrade is needed." )
                sys.exit(2)
            else:
                if int(ubuntu.read().strip()[13:-4]) < int(data['ubuntu_last_major_update']):
                    print("Your ubuntu version (" + ubuntu.read().strip()[7:-6]+ ") is the latest, but an upgrade is needed.")
                    sys.exit(1)
                else:
                    print("Your Ubuntu version (" + ubuntu.read().strip()[7:-4]+ ") is the latest one and up to date. All OK")

else:
    print("unkown OS")
    sys.exit(3)

