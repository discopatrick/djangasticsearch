from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ContactList.as_view(), name='contacts_contact_list'),
]
