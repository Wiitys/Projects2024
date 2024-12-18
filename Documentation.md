Laumonier Timothée  
Ciurlik Robin  
Walter Malcolm  
Dev1

**Documentation du projet**

**Projet** : Développement d'un jeu de dames en python

**Spécifications fonctionnelles :**

* **Description** : L'application permettra aux utilisateurs de jouer aux dames de façon fonctionnelle en 1vs1 à deux joueurs.  
* **Fonctionnalités principales** :  
  * Déplacer les pions  
  * Avoir une dame et la déplacer  
  * Manger les pions, rejouer derrière, gagner une partie  
* **Scénario d'utilisation** :  
  L'utilisateur ouvre l'application. Il décide de jouer contre un ami et ils se mettent ensemble sur le même pc. L’un joue les noirs, l’autre les blancs. Ils appuient sur le bouton Jouer et la partie se lance. ils déplacent les pions et le joueur 1 réussit à obtenir une dame. Mais finalement il perd et le pop-up de victoire affiche que les noirs ont gagné.  
* **Exigences spécifiques** :  
  * Un pion classique ne peut se déplacer qu’en avant sauf si il peut manger un pion ennemi  
  * Une dame se déplace librement en diagonale sur toutes les cases  
  * Selon le tour seule une couleur de pion peut se déplacer  
  * Affichage du nombre de pions et du tour  
* **Interfaces utilisateur** :  
  * Écran de la partie du jeu de dame

**Spécifications techniques :** 

#### **1\. Organisation du projet**

Le projet est structuré en deux principaux modules :

* **Backend** (logique métier) :  
  * `Plateau` : Gestion de l’état du plateau et des règles du jeu.  
  * Piece : Gestion de la logique des pièces sur le plateau  
* **Frontend** (interface utilisateur) :  
  * `Interface` : Gestion de l’affichage et de l’interaction utilisateur.  
* **`main.py`** : Point d’entrée du programme, où l’interface et la logique métier sont intégrées.

#### 

#### 

#### **2\. Dépendances**

Le projet repose sur :

* Python   
* Bibliothèques standard :  
  * `os` et `sys` pour la gestion des chemins.  
* Bibliothèques tierces :  
  * `tkinter` : Composants d’interface graphique.  
  * `customtkinter` : Extensions modernes pour les widgets Tkinter.

#### **3\. Architecture technique**

1. **Fichier `Plateau.py` (Backend) :**  
   * Responsable de l’initialisation du plateau et des règles de déplacement.  
   * Fonctions principales :  
     * `InitialiserPlateau` : Crée une grille avec les pions en position initiale.  
     * `GestionnaireDeMouvementPiece` : Vérifie et applique les déplacements.  
     * Gestion des promotions en dames (`PromotionReine`) et des captures (`ObtenirPositionIntermediaire`).  
2. **Fichier `Interface.py` (Frontend) :**  
   * Fournit l’interface utilisateur graphique pour afficher le jeu et gérer les événements.  
   * Utilise `CustomTkinter` pour des widgets modernes.  
   * Gère les interactions, comme le déplacement des pièces avec des événements `drag and drop`.  
3. **Fichier `main.py` (Point d’entrée) :**  
   * Charge la classe `Plateau` pour gérer l’état du jeu.  
   * Initialise une instance d’`InterfaceJeuDeDames` pour l’affichage.  
   * Lance l’application avec `fenetre.mainloop()`.

#### **4\. Communication entre les modules**

* **`Interface` communique avec `Plateau` pour :**  
  * Mettre à jour la grille après un déplacement.  
  * Valider les mouvements (simples ou captures).  
  * Alterner les tours entre les joueurs.  
* `Plateau` fournit des données (état de la grille, validation des mouvements) pour mettre à jour l’interface via des méthodes comme `ReafficherPieces`.

#### **5\. Exemple de flux d'exécution**

1. L’utilisateur ouvre l’application (`main.py`).  
2. La fenêtre `InterfaceJeuDeDames` est affichée.  
3. L’utilisateur sélectionne un pion (événement `<ButtonPress-1>`).  
4. Pendant le déplacement (événement `<B1-Motion>`), la position de la pièce est mise à jour en temps réel.  
5. Lors du relâchement (événement `<ButtonRelease-1>`), la logique métier de `Plateau` valide ou rejette le mouvement :  
   * Si valide : Le pion est déplacé, et les éventuelles captures ou promotions sont appliquées.  
   * Si invalide : Le pion revient à sa position initiale.

**6\. Normes de codage :** 

1. Utilisation de la norme PascalCase pour le nom des classes et fonctions  
2. Utilisation de la norme camelCase pour les variables et utilisation de préfixes (ex : v,p)

**Plans de test :**  
	