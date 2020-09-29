# check_os

## FRENCH

### Description
Ces scripts visent à

* Valider l’architecture 64bits
* Vérifier les versions d’OS (CentOS, Debian, Ubuntu)
* Retourner une erreur dans nagios en cas d’architecture 32bits et de version non mise à jour

Pour la version des OS, on utilise un fichier json stocké sur un serveur web. C’est ce fichier qu’il faut mettre à jour lorsqu’une nouvelle version d’OS est publiée

### Usage

#### Installer les dépendances nécessaires 
 apt install python3 python3-pip 
 
#### Installer distro 
 pip3 install distro

* Copier les scripts .py dans /opt/scripts/ 
* Copier le fichier mrpe.cfg dans le dossier /etc/check_mk/ 
* Copier le fichier os-version.json sur un serveur http
* Relancer xinetd 
* Relancer la decouverte de services dans l’interface web de check check_mk



## ENGLISH 

### Description
With this scripts you can 

 * Check if your OS is a 32 or 64bits
 * Check the linux distrib (CentOS, Debian, Ubuntu)
 * Get an error code (or not) in nagios Check_MK with mrpe.cfg file

For the OS version use the .json file on a web server. You have to update this file when a new version of an OS is released.


### Usage

#### Install the dependencies
 apt install python3 python3-pip
 
#### Install distro 
 pip3 install distro

* Copy scripts .py into /opt/scripts/ folder
* Copy mrpe.cfg file into /etc/check_mk/ folder
* Copy (and update if needed) os-version.json file on web server
* Restart xinetd 
* Restart check_mk discovery on the web interface of you check_mk server
