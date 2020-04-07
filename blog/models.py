# this page is used for databases

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title 
        
    # this class is created so that the page will redirect us to the post-detail page instead of error page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

