from django.urls import path
from . import views

"""
Definició de les rutes principals de l'aplicació blog.
"""

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("authors", views.authors),
    path("authors/<int:id>", views.author_detail),
    path("tags", views.tags),
    path("tags/<int:id>", views.tag_posts),
]
