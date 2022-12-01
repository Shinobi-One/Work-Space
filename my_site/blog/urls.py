from django.urls import path
from blog import views

urlpatterns = [

    path("", views.starting_page ,name = "home"),
    path("posts",views.posts, name = "posts"),
    path("posts/<slug:slug>",views.full_post, name = "full-post")
]