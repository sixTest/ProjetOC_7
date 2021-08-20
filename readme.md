#Description du projet

Ce projet est un problème d'optimisation combinatoire consistant à trouver la
meilleure combinaison d'actions pour des jeux de données particuliers en utilisant
un algorithme de force brute pour le jeu de données dataset_0 et un algorithme 
optimisé pour les jeux de données dataset_1 et dataset_2 avec une contrainte de temps (moins de 1 seconde)
et une contrainte de performance (les résultats de Sienna).

##Lancement des scripts
* Ouvrez un invite de commande
* Placez vous dans le dossier contenant les fichiers brute_force.py et optimized.py
* Création de l'environnement virtuel : ```python -m venv env```
* Activation de l'environnement virtuel :
    * Pour Windows : ```env\Scripts\activate.bat```
    * Pour Linux   : ```env/bin/activate```
* Installation des dépendances : ```pip install -r requirements.txt```
* Lancement des scripts : ```python <nom_script> <dataset> <investissement maximum>```
    * Exemple brute_force : ```python brute_force.py dataset_0.csv 500```
    * Exemple optimized : ```python optimized.py dataset_1.csv 500```
