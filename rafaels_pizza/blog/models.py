from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey("Category")
    content = models.TextField()

    def __str__(self):
        return "%s" % (self.title)
    
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.title)
