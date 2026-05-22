from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Author(models.Model):

    """
    Model que representa un autor del blog.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        """
        Retorna el nom complet de l'autor.
        """
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """
    Model que representa una etiqueta dels posts.
    """

    caption = models.CharField(max_length=20)

    def __str__(self):
        """
        Retorna el nom de l'etiqueta.
        """
        return self.caption


class Post(models.Model):
    """
    Model principal que representa un post del blog.
    """
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )

    excerpt = models.CharField(max_length=300)

    image_name = models.CharField(max_length=100)

    date = models.DateField(auto_now_add=True)

    slug = models.SlugField(unique=True)

    content = models.TextField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(
        Tag
    )

    def get_absolute_url(self):
        """
        Retorna la URL del detall del post.
        """
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        """
        Retorna el títol del post.
        """
        return self.title