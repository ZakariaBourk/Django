from django.contrib import admin
from .models import Author, Post, Tag

"""
Registre dels models del blog al panell d'administració de Django.
"""

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)