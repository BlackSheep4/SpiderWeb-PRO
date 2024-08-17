#!/bin/bash

# Ruta del proyecto local
PROJECT_PATH="/Users/alvaro/Desktop/PROJECTS/SPIDERWEB/spider-web-v2"

# Nombre del repositorio remoto en GitHub
REPO_NAME="SpiderWeb-PRO"
GITHUB_USER="BlackSheep4"
REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

# Nombre de la rama de desarrollo
BRANCH_NAME="dev"

# Función para inicializar el repositorio y hacer el push inicial
initialize_and_push() {
  cd $PROJECT_PATH || exit

  # Inicializar Git
  git init

  # Añadir archivos al staging area
  git add -A

  # Hacer el commit inicial
  git commit -m "Initial Commitment"

  # Verificar si el remoto 'origin' ya existe
  if git remote | grep origin > /dev/null; then
    echo "Remoto 'origin' ya existe, no se añadirá de nuevo."
  else
    # Añadir el repositorio remoto
    git remote add origin $REMOTE_URL
  fi

  # Crear y cambiar a la rama dev
  git checkout -B $BRANCH_NAME

  # Hacer pull de la rama remota para evitar conflictos (si existe)
  git pull origin $BRANCH_NAME --allow-unrelated-histories || echo "La rama remota $BRANCH_NAME no existe. Se omite el pull."

  # Hacer push al repositorio remoto
  git push -u origin $BRANCH_NAME
}

# Llamar a la función
initialize_and_push

echo "Repositorio inicializado y push realizado a $REMOTE_URL en la rama $BRANCH_NAME"
