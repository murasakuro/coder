from django.urls import path
from start.views import welcome

urlpatterns = [
    path('', welcome),
]
