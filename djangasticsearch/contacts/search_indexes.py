from haystack import indexes
from contacts.models import Contact

class ContactIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	first_name = indexes.CharField()
	last_name = indexes.CharField()

	def get_model(self):
		return Contact

	def index_queryset(self, using=None):
		# return the queryset of objects that will be indexed.
		# In this case, it's 'all' the contacts. In other cases,
		# e.g. blog posts, you'd want to index only the posts
		# that were already published, and not draft posts.
		return self.get_model().objects.all()
