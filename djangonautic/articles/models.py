from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	#attributes = fields
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.png", blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	#add in a author

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '...'

# python manage.py makemigrations
# python manage.py migrate


 