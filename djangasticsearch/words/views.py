from django.views.generic import ListView
from .models import Word

class WordList(ListView):
	model = Word
	paginate_by = 10
