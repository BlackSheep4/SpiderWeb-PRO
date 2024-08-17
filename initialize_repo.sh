#!/bin/bash

# Ruta del proyecto local
PROJECT_PATH="/Users/alvaro/Desktop/PROJECTS/SPIDERWEB/spider-web-v2"

# Nombre del repositorio remoto en GitHub
REPO_NAME="SpiderWeb-PRO"
GITHUB_USER="BlackSheep4"
REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

# Función para inicializar el repositorio y hacer el push inicial
initialize_and_push() {
  cd $PROJECT_PATH || exit

  # Inicializar Git
  git init

  # Añadir archivos al staging area
  git add -A

  # Hacer el commit inicial
  git commit -m "Initial Commitment"

  # Añadir el repositorio remoto
  git remote add origin $REMOTE_URL

  # Hacer pull de la rama remota para evitar conflictos
  git pull origin dev --allow-unrelated-histories

  # Hacer push al repositorio remoto
  git push -u origin dev
}

# Llamar a la función
initialize_and_push

echo "Repositorio inicializado y push realizado a $REMOTE_URL"