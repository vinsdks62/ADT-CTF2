#!/bin/bash
# Script de démarrage pour ADT-CTF

echo "[*] Création de l'environnement virtuel..."
python3 -m venv venv

echo "[*] Activation de l'environnement virtuel..."
source venv/bin/activate

echo "[*] Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Lancement des challenges..."
# Lancer chaque challenge dans un terminal séparé en arrière-plan
# Exemple avec Titan Originel
cd challenges/titan_originel
nohup python3 server.py > server.log 2>&1 &

cd ../../
echo "[*] Tous les challenges sont lancés."
echo "[*] Accédez maintenant aux interfaces web selon les instructions de chaque challenge."
