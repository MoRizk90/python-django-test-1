from django.db import models

# Create your models here.

class USER(models.Model):
    first_name = models.CharField(max_length = 264)
    seconed_name =  models.CharField(max_length = 264)
    email =  models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.first_name
