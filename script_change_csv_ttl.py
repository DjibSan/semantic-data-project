# Make sure to do :
# pip install rdflib
from rdflib import Graph,URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF
# pip install unidecode
import unidecode
import csv

#-----------------------------------------------------------------------------

# refs for the triples
incity = URIRef("http://sw-portal.deri.org/ontologies/swportal#inCity")
incountry = URIRef("http://sw-portal.deri.org/ontologies/swportal#inCountry")
iata = URIRef("https://data.nasa.gov/ontologies/atmonto/NAS#iataAirportCode")
icao = URIRef("https://data.nasa.gov/ontologies/atmonto/NAS#icaoAirportCode")
lat = URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")
long = URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")
alti = URIRef("http://dbpedia.org/ontology/altitude")
timezone = URIRef("http://vocab.org/transit/terms/timezone")
foaf_name = URIRef("http://xmlns.com/foaf/0.1/name")
rdfType = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#/type")
dboCity = URIRef("http://dbpedia.org/ontology/city")
dboCountry = URIRef("http://dbpedia.org/ontology/country")

# eachs airport, city, country, iata, icao is a ressource 
ressource = "http://fr.dbpedia.org/resource/"

f = open("airport2.ttl", "a")
g = Graph()


with open('airports.csv', newline='\n', encoding="utf-8") as csvfile: #ouvre le fichier csv
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader: # Pour chaque ligne
        ligne = []
        for item in row:

            # Normalisation pour éviter les erreurs
            item = item.replace(" ","_")
            item = item.replace("\"","")
            item = item.replace("\\","")
            item = item.replace("`","_")
            
            item = unidecode.unidecode(item)
            ligne.append(item) # passage en tbl

        # Création des triples
        g.add((URIRef(ressource+ligne[1]), foaf_name, Literal(ligne[1])))
        g.add((URIRef(ressource+ligne[1]), incity, Literal(ligne[2])))
        g.add((URIRef(ressource +ligne[2]), rdfType, dboCity))
        g.add((URIRef(ressource+ligne[1]), incountry, Literal(ligne[3])))
        g.add((URIRef(ressource +ligne[3]), rdfType, dboCountry))
        g.add((URIRef(ressource+ligne[1]), iata, URIRef(ressource +ligne[4])))
        g.add((URIRef(ressource+ligne[1]), icao, URIRef(ressource +ligne[5])))
        g.add((URIRef(ressource+ligne[1]), lat, Literal(ligne[6])))
        g.add((URIRef(ressource+ligne[1]), long, Literal(ligne[7])))
        g.add((URIRef(ressource+ligne[1]), alti, Literal(ligne[8])))
        g.add((URIRef(ressource+ligne[1]), timezone, Literal(ligne[9])))



f.write(g.serialize()) # écriture dans le fichier ttl
f.close()

#écrit par xavier houdart
