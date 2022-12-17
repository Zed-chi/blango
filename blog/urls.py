from django.urls import path

from . import views

urlpatterns = [
    path("post/<slug>", views.post_detail, name="blog-post-detail"),
    path("", views.index),
]
