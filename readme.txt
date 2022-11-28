Architecture du projet : 

Les dossiers :
    Arbre : Dossier principal du projet.
    applicant : Application comprenant la page d'accueil et la page "produit" du simplonien.
    account_simplonien : compte utilisateurs simplonien.

Toutes les redirections sont actuellement dans le fichier "urls.py" principal, si l'appli grossit il faudra rediriger vers des "urls.py" à chaque startapp.

SqLite contient actuellement uniquement le premier modèle afin de créer un profil par simplonien.