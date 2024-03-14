from django.urls import path
from . import views

urlpatterns = [
    path('book/details/<int:id>', views.details, name='details')
]
