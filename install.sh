#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}###############################################"
echo -e "#     INSTALLATION DU WHATSAPP TOOL           #"
echo -e "###############################################${NC}"

if ! command -v python3 &> /dev/null
then
    echo -e "${RED}[!] Python3 n'est pas installé. Installation en cours...${NC}"
    sudo apt-get update && sudo apt-get install -y python3 python3-pip
else
    echo -e "${GREEN}[V] Python3 est déjà présent.${NC}"
fi

echo -e "${CYAN}[*] Installation des dépendances via pip...${NC}"
pip3 install -r requirements.txt

if [ ! -d "sessions" ]; then
  mkdir sessions
  echo -e "${GREEN}[V] Dossier de session créé.${NC}"
fi

chmod +x DarkBomber.py

echo -e "${GREEN}###############################################"
echo -e "#    INSTALLATION TERMINÉE AVEC SUCCÈS           #"
echo -e "#    Lancer avec : python3 DarkBomber.py         #"
echo -e "###############################################${NC}"
