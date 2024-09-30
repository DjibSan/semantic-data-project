# Transformation de Données Ouvertes en Données Sémantiques

## Objectif du projet

Ce projet a pour objectif de transformer les données ouvertes en données sémantiques et de les lier au cloud de "Linked Data: Connect Distributed Data across the Web". Le projet suit plusieurs étapes et est réalisé en groupe.

## Structure du Projet

- **Étape 1 : Choix des données et transformation en données sémantiques**
  - Dataset choisi : **Airports, Airlines, Planes, and Routes** de Kaggle.
  - Transformation des données en RDF en utilisant les vocabulaires adaptés depuis le moteur de recherche LOV ([Linking Open Vocabularies](https://lov.linkeddata.es/dataset/lov/)).
  - Mise en place d'un serveur **Apache Jena Fuseki** pour héberger et interroger les données RDF.

- **Étape 2 : Requêtes SPARQL**
  - Nous avons proposé deux requêtes SPARQL intéressantes :
    - Requête 1 : [Lien vers query1.rq](queries/query1.rq)
    - Requête 2 : [Lien vers query2.rq](queries/query2.rq)

- **Étape 3 : Lier les données à celles des autres groupes**
  - Collaboration avec d'autres groupes pour lier les données sémantiques.

- **Étape 4 : Lier les données au Linked Data Cloud**
  - Ajout de propriétés et de liens pour connecter nos données au réseau de Linked Data.

- **Étape 5 : Description des datasets avec vocabulaire VOID**
  - Utilisation du vocabulaire VOID pour décrire les datasets RDF.

## Installation et Configuration de Fuseki

1. **Installation du serveur Fuseki** :
   Téléchargez et installez **Apache Jena Fuseki** en suivant les instructions [ici](https://jena.apache.org/documentation/fuseki2/).
   
2. **Configuration** :
   Copiez le fichier de configuration `config.ttl` dans le dossier `fuseki/` de ce dépôt.

3. **Lancement du serveur** :
   ```bash
   ./fuseki-server --config=fuseki/config.ttl
