import os, sys, json
import rdflib
import urllib2
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', 'lib'))
from pyld import jsonld

osuNs = rdflib.Namespace('http://data.library.oregonstate.edu/G/')
g = rdflib.ConjunctiveGraph()
theses = rdflib.Graph(g.store, osuNs.theses)

theses.parse(open('theses.nt'), format='nt')
thesis_ctx = json.load(urllib2.urlopen('http://achelo.us/thesis.jsonld'))
person_ctx = json.load(urllib2.urlopen('http://json-ld.org/contexts/person.jsonld'))

print jsonld.compact(jsonld.from_rdf(g.serialize(format='nquads')), [thesis_ctx, person_ctx])

