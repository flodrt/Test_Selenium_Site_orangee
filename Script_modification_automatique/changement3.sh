# Demander à l'utilisateur d'entrer le chemin du répertoire
echo "Veuillez indiquer le chemin du répertoire contenant les fichiers Python à modifier:"
read repertoire

# Vérifier si le répertoire existe
if [ ! -d "$repertoire" ]; then
    echo "Le répertoire spécifié n'existe pas."
    exit 1
fi

# Utilisez la commande sed pour effectuer les remplacements
find "$repertoire" -type f -name "*.py" -exec sed -i 's/find_element_by_name(/find_element(By.NAME, /g' {} +
find "$repertoire" -type f -name "*.py" -exec sed -i 's/find_element_by_link_text(/find_element(By.LINK_TEXT, /g' {} +
find "$repertoire" -type f -name "*.py" -exec sed -i 's/find_element_by_xpath(/find_element(By.XPATH, /g' {} +