

# 🧬 Jeu de la Vie (Game of Life) – Python & Pygame

Ce projet est une implémentation du **Jeu de la Vie** de John Conway en Python à l'aide de la bibliothèque **Pygame**.

## 🎮 Fonctionnement

Le **Jeu de la Vie** est un automate cellulaire à deux dimensions. Il se déroule sur une grille où chaque cellule peut être **vivante** ou **morte**. À chaque génération (itération), l'état des cellules est mis à jour en fonction de règles simples :

* Une cellule vivante avec **2 ou 3 voisins vivants** reste vivante.
* Une cellule morte avec **exactement 3 voisins vivants** devient vivante.
* Dans tous les autres cas, la cellule devient ou reste morte.

---

## 🧱 Structure du Code

### `Cell` (Classe)

Représente une cellule de la grille avec :

* `row`, `col` : ses coordonnées
* `alive` : état (vivante ou morte)

### `Grid` (Classe)

Gère la grille du jeu :

* Initialise les cellules
* Compte les voisins vivants (`get_alive_neighbors`)
* Applique les règles pour mettre à jour l'état des cellules (`update`)
* Peut initialiser la grille aléatoirement (`randomize`)

### `GameOfLife` (Classe)

Gère la logique du jeu :

* Démarre la simulation (`start`)
* Met à jour la grille à chaque tick (`update`)

### `Display` (Classe)

Gère l'affichage avec Pygame :

* Dessine la grille et les cellules
* Gère les événements (fermeture, pause, redémarrage aléatoire)

---

## ⚙️ Commandes Clavier

* **ESPACE** : Pause ou reprise de la simulation
* **R** : Réinitialiser la grille avec un état aléatoire

---

## ▶️ Lancer le programme

### 1. Installer Pygame (si ce n'est pas déjà fait)

```bash
pip install pygame
```

### 2. Lancer le script

```bash
python game_of_life.py
```

---

## 📐 Paramètres modifiables

Dans les premières lignes du fichier, vous pouvez ajuster :

```python
WIDTH, HEIGHT = 800, 600       # Dimensions de la fenêtre
CELL_SIZE = 10                 # Taille d'une cellule
FPS = 10                       # Vitesse de rafraîchissement (générations/seconde)
```

---

## 📸 Aperçu

À chaque tick, la grille évolue selon les règles du Jeu de la Vie. Les cellules vertes sont vivantes, les noires sont mortes. Une grille blanche est superposée pour plus de lisibilité.

---

## 🔁 Améliorations possibles

* Bouton de reset graphique
* Dessin manuel de cellules avec la souris
* Sauvegarde/chargement d'une configuration
* Grille torique (voisinage cyclique)
* Zoom ou redimensionnement dynamique

---

## 🧑‍💻 Auteur

Projet de simulation du **Jeu de la Vie** en Python – Exemple pédagogique.

---
