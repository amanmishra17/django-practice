from django.urls import path
from .views import home2

urlpatterns = [
    path('', home2),
]