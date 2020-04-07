# this page is used to see who makes the posts, the author and the post
from django.contrib import admin
from .models import Post

admin.site.register(Post)
