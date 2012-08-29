from django.conf import settings
from django.forms import Form, CharField
from django.shortcuts import render_to_response
from django import template
from pyes import *

def home(request, ref=None):
    search_form = SearchForm()
    return render_to_response("search.tpl", {'form':search_form})

def results(request, ref=None):
    form_input = SearchForm(request.GET)
    if form_input.is_valid():
        fields = form_input.cleaned_data
        results = _search("title", fields['searchText'])
    else:
        results = {}

    return render_to_response("results.tpl", {'results': results})

class SearchForm(Form):
    searchText = CharField()

def _search(query_type, term):
    conn = ES([settings.ES_HOST])
    query = TermQuery(query_type, term)
#    query.facet.add_term_facet('author')
    return conn.search(query)

