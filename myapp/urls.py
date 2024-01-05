from django.urls import path
from .views import hello_world, hello, world, home

urlpatterns=[
    path("hello/", hello),
    path("world/",world),
    path("",hello_world),
    path("home/", home),
]