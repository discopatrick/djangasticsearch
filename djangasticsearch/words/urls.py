from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.WordList.as_view(), name='words_word_list'),
]
