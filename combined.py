import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef, OWL
from rdflib.namespace import XSD
from urllib.parse import quote


MY_ONTOLOGY = Namespace("http://example.org/my_ontology/")

dataframe1= pd.read_csv("./reduced_dataset11.csv")
dataframe2 = pd.read_csv("./reduced_dataset2.csv")
df=pd.merge(dataframe1, dataframe2, on=['Title','ID'], how="inner")


g = Graph()


g.add((MY_ONTOLOGY.ID, RDF.type, OWL.Class))
g.add((MY_ONTOLOGY.Title, RDF.type, OWL.Class))
g.add((MY_ONTOLOGY.ReleaseYear, RDF.type, OWL.Class))
g.add((MY_ONTOLOGY.Locations, RDF.type, OWL.Class))
g.add((MY_ONTOLOGY.Cast, RDF.type, OWL.Class))
g.add((MY_ONTOLOGY.Crew, RDF.type, OWL.Class))





g.add((MY_ONTOLOGY.DirectedBy,RDF.type,OWL.DatatypeProperty))
g.add((MY_ONTOLOGY.DirectedBy, RDFS.domain, MY_ONTOLOGY.Title))
g.add((MY_ONTOLOGY.DirectedBy, RDFS.range, XSD.string))
g.add((MY_ONTOLOGY.DistributedBy,RDF.type,OWL.DatatypeProperty))
g.add((MY_ONTOLOGY.DistributedBy, RDFS.domain, MY_ONTOLOGY.Title))
g.add((MY_ONTOLOGY.DistributedBy, RDFS.range, XSD.string))
g.add((MY_ONTOLOGY.ProducedBy,RDF.type,OWL.DatatypeProperty))
g.add((MY_ONTOLOGY.ProducedBy, RDFS.domain, MY_ONTOLOGY.Title))
g.add((MY_ONTOLOGY.ProducedBy, RDFS.range, XSD.string))
g.add((MY_ONTOLOGY.WrittenBy,RDF.type,OWL.DatatypeProperty))
g.add((MY_ONTOLOGY.WrittenBy, RDFS.domain, MY_ONTOLOGY.Title))
g.add((MY_ONTOLOGY.WrittenBy, RDFS.range, XSD.string))

g.add((MY_ONTOLOGY.ShotLocation, RDF.type, OWL.ObjectProperty))
g.add((MY_ONTOLOGY.ShotLocation, RDFS.domain, MY_ONTOLOGY.Locations))
g.add((MY_ONTOLOGY.ShotLocation, RDFS.range, MY_ONTOLOGY.Title))

g.add((MY_ONTOLOGY.ActedIn, RDF.type, OWL.ObjectProperty))
g.add((MY_ONTOLOGY.ActedIn, RDFS.domain, MY_ONTOLOGY.Cast))
g.add((MY_ONTOLOGY.ActedIn, RDFS.range, MY_ONTOLOGY.Title))

g.add((MY_ONTOLOGY.WorkedWith, RDF.type, OWL.ObjectProperty))
g.add((MY_ONTOLOGY.WorkedWith, RDFS.domain, MY_ONTOLOGY.Cast))
g.add((MY_ONTOLOGY.WorkedWith, RDFS.range, MY_ONTOLOGY.Crew))


for i,row in df.iterrows():
        id_uri=URIRef(quote(f"{MY_ONTOLOGY}Row_ID{row['ID']}"))
        g.add((id_uri, RDF.type, MY_ONTOLOGY.ID))
        g.add((id_uri, MY_ONTOLOGY.ID, Literal(row['ID'])))


        title_uri2=URIRef(quote(f"{MY_ONTOLOGY}Title{row['Title']}"))
        g.add((title_uri2, RDF.type, MY_ONTOLOGY.Title))
        g.add((title_uri2, RDFS.label, Literal(row['Title'],datatype=XSD.string)))
        g.add((title_uri2, MY_ONTOLOGY.DirectedBy, Literal(row['Director'],datatype=XSD.string )))
        g.add((title_uri2, MY_ONTOLOGY.DistributedBy, Literal(row['Distributor'],datatype=XSD.string )))
        g.add((title_uri2, MY_ONTOLOGY.ProducedBy, Literal(row['Production Company'],datatype=XSD.string )))
        g.add((title_uri2, MY_ONTOLOGY.WrittenBy, Literal(row['Writer'],datatype=XSD.string )))

        releaseyear_uri = URIRef(quote(f"{MY_ONTOLOGY}ReleaseYear{row['Release Year']}"))
        g.add((releaseyear_uri, RDF.type, MY_ONTOLOGY.ReleaseYear))
        g.add((releaseyear_uri, RDFS.label, Literal(row['Release Year'],datatype=XSD.integer)))
        g.add((releaseyear_uri, MY_ONTOLOGY.ReleaseYear, Literal(row['Release Year'])))


        locations_uri = URIRef(quote(f"{MY_ONTOLOGY}Locations{row['Locations']}"))
        g.add((locations_uri, RDF.type, MY_ONTOLOGY.Locations))
        g.add((locations_uri, RDFS.label, Literal(row['Locations'],datatype=XSD.string)))

        g.add((MY_ONTOLOGY.Actor1,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.Actor1,RDFS.subClassOf,MY_ONTOLOGY.Cast))
        actor1_uri = URIRef(quote(f"{MY_ONTOLOGY}Actors{row['Actor1']}"))
        g.add((actor1_uri, RDF.type, MY_ONTOLOGY.Actor1))
        g.add((actor1_uri, RDFS.label, Literal(row['Actor1'],datatype=XSD.string)))

        g.add((MY_ONTOLOGY.Actor2,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.Actor2,RDFS.subClassOf,MY_ONTOLOGY.Cast))
        actor2_uri = URIRef(quote(f"{MY_ONTOLOGY}Actors{row['Actor2']}"))
        g.add((actor2_uri, RDF.type, MY_ONTOLOGY.Actor2))
        g.add((actor2_uri, RDFS.label, Literal(row['Actor2'],datatype=XSD.string)))

        g.add((MY_ONTOLOGY.Director,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.Director,RDFS.subClassOf,MY_ONTOLOGY.Crew))
        Director_uri = URIRef(quote(f"{MY_ONTOLOGY}Director{row['Director']}"))
        g.add((Director_uri, RDF.type, MY_ONTOLOGY.Director))
        g.add((Director_uri, RDFS.label, Literal(row['Director'],datatype=XSD.string)))

        g.add((MY_ONTOLOGY.Distributor,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.Distributor,RDFS.subClassOf,MY_ONTOLOGY.Crew))
        Distributor_uri = URIRef(quote(f"{MY_ONTOLOGY}Distributed By{row['Distributor']}"))
        g.add((Distributor_uri, RDF.type, MY_ONTOLOGY.Distributor))
        g.add((Distributor_uri, RDFS.label, Literal(row['Distributor'],datatype=XSD.string)))

        g.add((MY_ONTOLOGY.ProductionCompany,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.ProductionCompany,RDFS.subClassOf,MY_ONTOLOGY.Crew))
        produced_by = URIRef(quote(f"{MY_ONTOLOGY}Produced By{row['Production Company']}"))
        g.add((produced_by, RDF.type, MY_ONTOLOGY.ProductionCompany))
        g.add((produced_by, RDFS.label, Literal(row['Production Company'],datatype=XSD.string)))

        
        g.add((MY_ONTOLOGY.Writer,RDF.type,OWL.Class))
        g.add((MY_ONTOLOGY.Writer,RDFS.subClassOf,MY_ONTOLOGY.Crew))
        writer_uri = URIRef(quote(f"{MY_ONTOLOGY}Written By{row['Writer']}"))
        g.add((writer_uri, RDF.type, MY_ONTOLOGY.Writer))
        g.add((writer_uri, RDFS.label, Literal(row['Writer'],datatype=XSD.string)))

g.serialize(destination='example.rdf', format='xml')


