# Importation des bibliothèques nécessaires
from rdflib import Graph, URIRef
from rdflib.namespace import OWL

dbpedia_resource = "http://fr.dbpedia.org/resource/"
schema_resource = "http://schema.org/"
wikidata_resource = "https://www.wikidata.org/wiki/"
g = Graph()
g.parse("airport.ttl",format="turtle")

for airport in g.subjects():
   
    if dbpedia_resource in str(airport):
        dbpedia_airport_uri = URIRef(f"http://dbpedia.org/resource/{airport.split('/')[-1]}")
        g.add((airport, OWL.sameAs, dbpedia_airport_uri))
        schema_airport_uri = URIRef(f"{schema_resource}Airport")

        g.add((airport, OWL.sameAs, schema_airport_uri))
        country = g.value(airport, URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#country"))
        if country:
            country_uri = URIRef(f"{dbpedia_resource}{country.replace(' ', '_')}")
            g.add((airport, OWL.sameAs, country_uri))
            g.add((country_uri, RDF.type, URIRef("http://dbpedia.org/ontology/Country")))

            # Ajout d'un lien vers Wikidata pour le pays
            wikidata_country_uri = URIRef(f"{wikidata_resource}{country.replace(' ', '_')}")
            g.add((country_uri, OWL.sameAs, wikidata_country_uri))
    

with open("linked_airport.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
