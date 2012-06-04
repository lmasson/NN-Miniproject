# Question 1.1:

Repris le module hopfield.py en y apportant quelques modifications afin de le faire correspondre au modèle décrit au début de l'énoncé.

Changements :
	- Au lieu de créer des réseaux de taille NxN (et donc des matrices de poids de taille N^2xN^2), on doit ici créer un réseau de taille N (et donc une matrice de poid simplement NxN).
	- Apporter les modifications pour qu'on affiche l'évolution de l'énergie et de l'overlap sur les 2 premiers pas de temps pour un pattern.
	- Toutes les multiplications entre vecteurs à l'aide de la fonction sum() sont réécrites pour plutôt utiliser la fonction dot(). Gain de rapidité dans l'exécution.