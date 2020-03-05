from django.urls import path
from .views import (
#    SavedDataListView,
    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
    ApartmentDeleteView
)
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('apartment/', views.apartment, name='apartment'),
	path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
	path('apartment/new/', ApartmentCreateView.as_view(), name='apartment-create'),
	path('apartment/<int:pk>/update/', ApartmentUpdateView.as_view(), name='apartment-update'),
	path('apartment/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='apartment-delete'),
]
