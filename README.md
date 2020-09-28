# check_os

=Description=

Ces scripts visent à

* Valider l’architecture 64bits
* Vérifier les versions d’OS (CentOS, Debian, Ubuntu)
* Retourner une erreur dans nagios en cas d’architecture 32bits et de version non mise à jour

Pour la version des OS, on utilise un fichier json stocké sur un serveur web. C’est ce fichier qu’il faut mettre à jour lorsqu’une nouvelle version d’OS est publiée

=Usage=

Installer les dépendances nécessaires 

 apt install python3 python3-pip 
 pip3 install distro

* Copier les scripts .py dans /opt/scripts/ 
* Copier le fichier mrpe.cfg dans le dossier /etc/check_mk/ 
* Copier le fichier os-version.json sur un serveur http
* Relancer xinetd 
* Relancer la decouverte de services dans l’interface web de check check_mk
