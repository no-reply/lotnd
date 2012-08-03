import os, sys, json
import rdflib
import urllib2
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', 'lib'))
from pyld import jsonld
from SPARQLWrapper import SPARQLWrapper, JSON, XML

endpoint = SPARQLWrapper("http://data.library.oregonstate.edu:8080/sparql/")
endpoint.setReturnFormat(JSON)
osuNs = rdflib.Namespace('http://data.library.oregonstate.edu/G/')
outfile = open('theses.json', 'w')
outfile_f = open('theses_f.json', 'w')

# get list of theses
listQuery = "SELECT ?thesis WHERE { ?thesis <http://www.w3.org/2000/01/rdf-schema#type> <http://purl.org/ontology/bibo/Thesis> . }"
endpoint.setQuery(listQuery)
theses = endpoint.query().convert()['results']['bindings']
item_count = len(theses)

try:
    contexts = []
    contexts.append(json.load(urllib2.urlopen('http://achelo.us/thesis.jsonld')))
except urllib2.URLError:
    contexts = []
    print 'could not resolve context URIs. using local contexts.'
    contexts.append(open('thesis.jsonld', 'r'))

for thesis in theses[1:10]:
    g = rdflib.ConjunctiveGraph()
    #theses = rdflib.Graph(g.store, osuNs.theses) #reset graph
    uri = thesis['thesis']['value']
    thesisQuery = "DESCRIBE <" + uri + ">" 
    endpoint.setQuery(thesisQuery)
    endpoint.setReturnFormat(XML)
    thesisXML = endpoint.query().convert()
    #add the thesis to the temporary graph
#    print thesisXML.serialize(format='n3')
    tmpgraph = rdflib.Graph(g.store, osuNs['theses'])
    tmpgraph.parse(data=thesisXML.serialize(format='xml'))

    for o in tmpgraph.objects():
        if isinstance(o, rdflib.URIRef):
            query = "DESCRIBE <" + o + ">"
            endpoint.setQuery(query)
            desc = endpoint.query().convert()
            tmpgraph.parse(data=desc.serialize(format='xml'))

    j = jsonld.compact(jsonld.from_rdf(g.serialize(format='nquads')), contexts)
    outfile.write(json.dumps(j, indent=1))
    j = jsonld.frame(j, json.load(urllib2.urlopen('http://achelo.us/thesis_frame.jsonld')))
    outfile_f.write(json.dumps(j, indent=1))

outfile.close()
outfile_f.close()
