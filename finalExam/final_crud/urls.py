from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/', views.insert),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update)
]