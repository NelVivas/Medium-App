from django.db import models

from users.models import PersonalUser
from categories.models import Category

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
 

    creation_date = models.DateTimeField(auto_now_add = True)
    header_image = models.ImageField(upload_to = 'headerImages/', default = '')

    author = models.ForeignKey(PersonalUser,
            related_name = 'articles', 
            on_delete = models.CASCADE)

    category = models.ForeignKey(Category,
            related_name = 'articles',
            on_delete = models.CASCADE)

