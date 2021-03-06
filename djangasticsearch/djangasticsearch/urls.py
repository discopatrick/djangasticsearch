"""djangasticsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import haystack.urls as haystack_urls

import contacts.urls as contact_urls
import words.urls as word_urls
import search.urls as search_urls
from contacts.views import ContactList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^haystack-default-search/', include(haystack_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^word/', include(word_urls)),
    url(r'^$', ContactList.as_view()),
]
