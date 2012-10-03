import os, sys, json
import json
import rdflib
import urllib2
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', 'lib'))
from pyld import jsonld
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from pyes import *

endpoint = SPARQLWrapper("http://data.library.oregonstate.edu:8080/sparql/")
endpoint.setReturnFormat(JSON)
osuNs = rdflib.Namespace('http://data.library.oregonstate.edu/G/')
outfile = open('theses.json', 'w')
outfile_f = open('theses_f.json', 'w')
outfile_e = open('theses_errors.json', 'w')
mapping = json.loads(open('thesis.mapping.json', 'r').read())

elastic = ES('http://data.library.oregonstate.edu:9200')
elastic.delete_index_if_exists('theses')
elastic.create_index('theses')
elastic.put_mapping('thesis', {'properties':mapping}, ['theses'])

# get list of theses
listQuery = "SELECT ?thesis WHERE { ?thesis <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/ontology/bibo/Thesis> . }"
endpoint.setQuery(listQuery)
theses = endpoint.query().convert()['results']['bindings']
item_count = len(theses)
count = 0

try:
    contexts = []
    contexts.append(json.load(urllib2.urlopen('http://achelo.us/thesis.jsonld')))
except urllib2.URLError:
    contexts = []
    print 'could not resolve context URIs. using local contexts.'
    contexts.append(open('thesis.jsonld', 'r'))

for thesis in theses:
    count += 1
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
    if 0 in j['@graph']:
        try:
            outfile.write(json.dumps(j['@graph'][0], indent=1))
            j = jsonld.frame(j, json.load(urllib2.urlopen('http://achelo.us/thesis_frame.jsonld')))
            outfile_f.write(json.dumps(j['@graph'][0], indent=1))
            elastic.index(j['@graph'][0], 'theses', 'thesis')
        except Exception as e:
            print e 
            print json.dumps(j['@graph'])
            outfile_e.write(json.dumps(j))
            continue

    if (count % 100) == 0:
        print count

outfile.close()
outfile_f.close()
