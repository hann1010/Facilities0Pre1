from django.urls import path
from .views import (
#    SavedDataListView,
    ApartmentDetailView,
#    SavedDataCreateView,
#    SavedDataUpdateView,
#    SavedDataDeleteView
)
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('apartment/', views.apartment, name='apartment'),
	path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
]
