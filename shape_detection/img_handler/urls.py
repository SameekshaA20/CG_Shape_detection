from django.urls import path
from .views import uploadForm
urlpatterns = [
    path('',uploadForm)
]