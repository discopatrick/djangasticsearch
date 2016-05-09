from django.shortcuts import render

from haystack.generic_views import SearchView
from haystack.forms import SearchForm

class ContactSearch(SearchView):
	template_name = 'search/search-generic-view.html'
	form_class = SearchForm

class WordSearch(SearchView):
	template_name = 'search/search-generic-view.html'
	form_class = SearchForm
