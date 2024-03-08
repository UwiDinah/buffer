from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title