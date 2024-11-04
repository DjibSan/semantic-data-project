from rdflib import Graph, URIRef
from rdflib.namespace import OWL

ressource = "http://fr.dbpedia.org/resource/"

g = Graph()
g.parse("airport.ttl",format="turtle")

for airport in g.subjects():
   
    if ressource in str(airport):
        dbpedia_airport_uri = URIRef(f"http://dbpedia.org/resource/{airport.split('/')[-1]}")
        g.add((airport, OWL.sameAs, dbpedia_airport_uri))
          g.add((dbpedia_airport_uri, RDF.type, URIRef("http://dbpedia.org/ontology/Airport")))

with open("linked_airport.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
