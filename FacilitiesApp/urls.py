from django.urls import path
from .views import (
#    SavedDataListView,
#    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
    ApartmentDeleteView,
	TicketCreateView,
	TicketUpdateView,
	TicketPreCreateView,
)
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('filter/', views.home, name='home-filter'),
	path('apartment/', views.apartment, name='apartment'),
	path('apartment/new/', ApartmentCreateView.as_view(), name='apartment-create'),
	path('apartment/<int:pk>/update/', ApartmentUpdateView.as_view(), name='apartment-update'),
	path('apartment/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='apartment-delete'),
	path('ticket/new/', TicketCreateView.as_view(), name='ticket-create'),
	path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),
	path('apartment/<int:pk>/to-ticket/pre-new/', TicketPreCreateView.as_view(), name='pre-ticket-create'),
]
