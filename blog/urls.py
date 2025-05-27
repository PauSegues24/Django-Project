from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='Starting-Page'),
    path('posts/', views.posts, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path('authors', views.authors, name='author_list'),
    path('authors/<str:first_name>/<str:last_name>/', views.author_detail, name='author-detail'),
    path('tags', views.tags, name='tag_list'),
    path('tags/<tag>', views.tag_detail, name='tag-detail'),
]