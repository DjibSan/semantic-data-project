# Projet de Transformation de Données Ouvertes en Données Sémantiques

## Objectif du projet

L'objectif de ce projet est de transformer un jeu de données ouvertes en données sémantiques et de les lier au cloud "Linked Data : Connect Distributed Data across the Web". Le projet inclut plusieurs étapes, telles que la transformation des données, l'installation d'un serveur local pour héberger les données sémantiques, et l'exécution de requêtes SPARQL pour interroger ces données.

## Données utilisées

Bien que le dataset choisi comporte quatre fichiers, nous avons décidé de nous concentrer exclusivement sur **Airports.csv**. Ce fichier contient des informations détaillées sur les aéroports du monde entier, notamment :

- **Nom de l'aéroport** : Le nom officiel de l'aéroport.
- **Code IATA/ICAO** : Codes standardisés pour identifier les aéroports.
- **Localisation géographique** : Latitude, longitude, et altitude.
- **Ville et pays** : Localisation géographique de l'aéroport.

Les autres fichiers du dataset (Airlines.csv, Planes.csv, Routes.csv) contiennent des informations sur les compagnies aériennes, les modèles d'avions et les routes, mais pour ce projet, nous allons nous concentrer uniquement sur la transformation et l'interrogation des données contenues dans **Airports.csv**.

## Étapes du projet

1. **Choix du dataset** : Nous avons sélectionné le dataset **Airports, Airlines, Planes, and Routes** pour sa richesse et sa pertinence dans le domaine de l'aviation mondiale.
2. **Focalisation sur Airports.csv** : Malgré les autres fichiers du dataset, nous avons choisi de travailler uniquement sur les données des aéroports pour simplifier l'analyse et mieux comprendre les caractéristiques géographiques des aéroports dans le monde.
3. **Transformation en données sémantiques** : Nous avons transformé les données de **Airports.csv** en RDF (Resource Description Framework) en utilisant des vocabulaires standards.
4. **Requêtes SPARQL** : Après avoir transformé les données, nous avons mis en place un serveur **Apache Jena Fuseki** pour héberger les données et exécuter des requêtes SPARQL afin d'extraire des informations pertinentes sur les aéroports.
   
## Source des données

- **Kaggle Dataset** : [Airports, Airlines, Planes, and Routes](https://www.kaggle.com/datasets/ahmadrafiee/airports-airlines-planes-and-routes-update-2024)

## Licence


