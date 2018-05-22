from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'index.html', {'cats': cats})

class Cat:
	def __init__(self, name, breed, description, age):
		self.name = name
		self.breed = breed
		self.description = description
		self.age = age

cats = [
	Cat('Toby', 'tabby', 'foul little demon', 3),
	Cat('Layla', 'tortoise shell', 'diluted tortoise shell', 12),
	Cat('Mouse', 'calico', 'annoying and loud', 7),
]