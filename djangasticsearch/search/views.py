from django.shortcuts import render

from haystack.generic_views import SearchView

class ContactSearch(SearchView):
	template_name = 'search/search-generic-view.html'
