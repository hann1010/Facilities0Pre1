from django.urls import path
#from .views import (
#    SavedDataListView,
#    SavedDataDetailView,
#    SavedDataCreateView,
#    SavedDataUpdateView,
#    SavedDataDeleteView
#)
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('apartment/', views.apartment, name='apartment'),
]
