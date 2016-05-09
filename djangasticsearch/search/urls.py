from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ContactSearch.as_view(), name='search_contact_search'),
    url(r'^word/$', views.WordSearch.as_view(), name='search_word_search'),
]
