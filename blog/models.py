from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title