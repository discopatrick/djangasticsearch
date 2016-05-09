from haystack import indexes
from .models import Word

class WordIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	word_string = indexes.CharField(model_attr='word_string')

	def get_model(self):
		return Word

	def index_queryset(self, using=None):
		# return the queryset of objects that will be indexed.
		# In this case, it's 'all' the contacts. In other cases,
		# e.g. blog posts, you'd want to index only the posts
		# that were already published, and not draft posts.
		return self.get_model().objects.all()
