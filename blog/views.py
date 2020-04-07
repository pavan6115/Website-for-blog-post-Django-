from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.http import HttpResponse      #use when you want to return something from HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    ordering = ['-date_posted'] # this will show the posts which is the recent one, the lastest
    paginate_by = 2       # this will display only 2 posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    paginate_by = 2 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # created this function so that whenever we try to post, set the logged in user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # created this function so that whenever we try to post, set the logged in user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # created this function so that other user cannot edit/update the post of the other users
    # only the valid user can update/edit his own posts and not of other users
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # this gets the current logged in user and check if both are same or not, if true allow to update
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # this gets the current logged in user and check if both are same or not, if true allow to update
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})