from django.db import models

class UserProfile(models.Model):
    username = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    linkedin = models.URLField()
    image = models.ImageField(upload_to='profile_pics/')
    company_link = models.URLField()

    def __str__(self):
        return self.name

