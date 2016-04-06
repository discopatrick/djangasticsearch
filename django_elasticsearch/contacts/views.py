from django.views.generic import ListView
from .models import Contact

class ContactList(ListView):
	model = Contact
	paginate_by = 10
