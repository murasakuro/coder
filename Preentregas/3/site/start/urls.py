from django.urls import path, include
from start.views import welcome, dice

urlpatterns = [
    path('', welcome),
    path('dados/', dice),
]
