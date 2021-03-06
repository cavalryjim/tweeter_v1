# tweets/views.py.  eafd33f7-08b3-4726-99c0-92b7abe3b5f0
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Tweet

class TweetListView(ListView):
    model = Tweet
    template_name = 'home.html'

class TweetCreateView(CreateView):
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')
