
from django.contrib import admin
from django.urls import path, include
from myapp.views import hello_world, hello, world

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('myapp.urls') ),
    path("crud/",include('forms.urls')),
]
