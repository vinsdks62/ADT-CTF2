#!/bin/bash
set -e

echo "[*] Création du virtualenv pour Titan Originel si nécessaire..."
if [ ! -d "venv_titan" ]; then
    python3 -m venv venv_titan
fi

echo "[*] Activation du virtualenv..."
source venv_titan/bin/activate

echo "[*] Installation des dépendances Python..."
pip install --upgrade pip
pip install -r challenges/titan_originel/requirements.txt
pip install requests beautifulsoup4

echo "[*] Démarrage des challenges PHP et Python en arrière-plan..."

# SQLi Shiganshina
if [ -f "challenges/sqli_shiganshina.php" ]; then
    php -S 0.0.0.0:8000 challenges/sqli_shiganshina.php > /tmp/sqli_shiganshina.log 2>&1 &
    echo "[*] SQLi Shiganshina lancé sur http://localhost:8000"
fi

# Titan Colossal
if [ -f "challenges/titan_colossal.php" ]; then
    php -S 0.0.0.0:8001 challenges/titan_colossal.php > /tmp/titan_colossal.log 2>&1 &
    echo "[*] Titan Colossal lancé sur http://localhost:8001/titan_colossal.php"
fi

# XSS Mur Maria
if [ -f "challenges/xss_mur_maria.php" ]; then
    php -S 0.0.0.0:8002 challenges/xss_mur_maria.php > /tmp/xss_mur_maria.log 2>&1 &
    echo "[*] XSS Mur Maria lancé sur http://localhost:8002/xss_mur_maria.php"
fi

# Titan Originel (Flask)
if [ -f "challenges/titan_originel/server.py" ]; then
    cd challenges/titan_originel
    nohup python3 server.py > server.log 2>&1 &
    cd ../..
    echo "[*] Titan Originel lancé sur http://localhost:9000"
    echo "[*] Logs Python de Titan Originel : challenges/titan_originel/server.log"
fi

echo "[*] Tous les challenges sont lancés !"
echo "[*] Vous pouvez continuer à utiliser votre terminal."

# --- Ouverture automatique de la page d'accueil ---
ACCUEIL_PATH="$(pwd)/accueil.html"

echo "[*] Ouverture automatique de la page d'accueil dans ton navigateur..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$ACCUEIL_PATH" >/dev/null 2>&1 || echo "[!] Impossible d'ouvrir le navigateur automatiquement. Ouvre $ACCUEIL_PATH manuellement."
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open "$ACCUEIL_PATH" >/dev/null 2>&1
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start "" "$ACCUEIL_PATH"
else
    echo "[!] OS non supporté pour l'ouverture automatique. Ouvre $ACCUEIL_PATH manuellement."
fi
