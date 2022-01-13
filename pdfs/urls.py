from django.urls import path

from . import views

urlpatterns = [
    path('bookings/', views.bookings_pdf, name='pdf_booking_list'),
    path('booking/confirm/<booking_id>', views.booking_confirm, name="pdf_booking_confirm"),

    # yacht types
    path('yachts/', views.yachts, name='pdf_yacht_list'),
    path('yachts/types', views.yacht_type, name='pdf_yacht_type_list'),

    path('packages/', views.packages, name='pdf_package_list'),
    path('events/', views.events, name='pdf_event_list'),
    path('events/bookings', views.event_bookings, name='pdf_event_booking_list'),

    path('trainings/', views.trainings, name='pdf_training_list'),
    path('trainings/bookings', views.training_bookings, name='pdf_training_booking_list'),


    path('employees/', views.employees, name='pdf_employees_list'),
    path('feedbacks/', views.feedbacks, name='pdf_feedbacks_list'),





    

]
