from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Чернетка"),
    (1,"Опубліковано")
)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Розділ"

    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    categories = models.ManyToManyField(Category, related_name="post_categories")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Допис"

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=60)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_to_post')

    def __str__(self):
        return f"{self.author} прокоментував '{self.post}'"