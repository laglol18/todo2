from django.views.generic import TemplateView, ListView

from .models import Post


class HomePageView(TemplateView):
    model = Post
    z = 'home.html'
    con = 'all_posts_list'
class AboutPageView(TemplateView):
    x = 'about.html'
    model = Post