from django.urls import path
from ragamath import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]