# Question 1.2

Overlap varie entre -1 et 1. 1 correspond à "tous les pixels sont les mêmes que ceux du pattern", et -1 correspond à "aucun pixel n'est en commun avec le pattern". Ainsi, le pourcentage de pixel qui correspondent au pattern vaut:

		100 x (overlap+1)/2

Pour avoir le nombre de pixels qui diffèrent par rapport au pattern, on calcule donc:

		100 x (1 - (overlap+1)/2 )