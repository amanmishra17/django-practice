from django.urls import path
from .views import SignUp
from first_app.views import index

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]