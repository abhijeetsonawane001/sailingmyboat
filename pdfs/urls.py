from django.urls import path

from . import views

urlpatterns = [
    path('bookings/', views.bookings_pdf, name='pdf_booking_list')
]
