#!/bin/bash
echo "[*] Installation des composants..."
pkg update && pkg upgrade -y
pkg install python nodejs git chromium -y
pip install -r requirements.txt
npm install whatsapp-web.js qrcode-terminal
chmod +x main.py
echo "[V] Prêt à l'emploi !"
