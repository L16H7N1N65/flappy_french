# Flappy French

<div align="center">
  
https://github.com/L16H7N1N65/flappy_french/assets/79063770/4f5e3896-c291-4594-a78d-1aee0e9ab35c

</div>


## Introduction
Flappy French est un jeu développé à des fins éducatives et pour pratiquer le développement logiciel. Il s'inspire des élections législatives suivant la dissolution du gouvernement par le Président de la République. Le jeu ne véhicule aucun message politique ni affiliation, mais utilise ce scénario comme toile de fond pour exercer des compétences techniques.

## Gameplay
Le jeu est similaire à Flappy Bird, où les joueurs contrôlent un oiseau (représentant un candidat) à travers des obstacles (tuyaux), en utilisant la barre de controle pour le maintenir en vol et éviter les collisions. Voici les principales fonctionnalités et étapes du jeu :

1. **Écran de démarrage** 

2. **Sélection de l'oiseau** 

3. **Sélection de la difficulté** 
  
4. **Jeu principal** 
  
5. **Fin de jeu** 
  

## Technologies utilisées
Le jeu est développé en utilisant Python et Pygame, une bibliothèque populaire pour le développement de jeux en 2D avec Python. Pygame facilite la gestion des graphismes, de l'audio et des interactions utilisateur dans le jeu.

## Structure du projet
Le projet est organisé comme suit :

- **main.py** : Point d'entrée du jeu. Initialise Pygame, gère les événements et les transitions entre les différents écrans (écran de démarrage, sélection de l'oiseau, sélection de la difficulté, jeu principal, écran de fin de jeu).
  
- **bird.py** : Définition de la classe `Bird`, qui représente l'oiseau contrôlé par le joueur. Gère le mouvement de l'oiseau, y compris le saut et la gravité.

- **pipe.py** : Définition de la classe `Pipe`, qui représente les tuyaux à éviter dans le jeu. Gère la génération aléatoire des tuyaux et leur défilement à l'écran.

- **game.py** : Contient les fonctions principales du jeu, telles que l'initialisation de l'écran, le dessin des éléments, la gestion des événements et la logique du jeu (détection de collisions, mise à jour du score, etc.).


## Auteur
Ce jeu a été développé par L16H7N1N65 https://github.com/L16H7N1N65/flappy_french

## Avertissement
Ce jeu est une simulation inspirée d'événements réels mais n'a aucune intention politique ou partisane. Il est destiné uniquement à des fins éducatives et de pratique du développement logiciel.



"""
    Flappy French Game
    Copyright (C) 2024  L16H7N1N65

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    You can contact me at linda.meghouche@gmail.com
"""

