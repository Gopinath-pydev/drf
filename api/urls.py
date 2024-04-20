from django.urls import path
from .views import home, individual

urlpatterns = [
    path('home/', home),
    path('individual/<int:id>', individual)
]