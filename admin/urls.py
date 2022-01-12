from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='admin_dashboard'),
    # Yachts
    path('yacht/types', views.yacht_type_list, name='admin_yacht_type_list'),
    path('yacht/types/add', views.yacht_type_add, name='admin_yacht_type_add'),
    path('yacht/types/edit/<slug>', views.yacht_type_edit, name="admin_yacht_type_edit"),
    path('yacht/types/delete/<slug>', views.yacht_type_delete, name="admin_yacht_type_delete"),

    path('yacht/', views.yacht_list, name="admin_yacht_list"),
    path('yacht/add', views.yacht_add, name="admin_yacht_add"),
    path('yacht/edit/<pk>', views.yacht_edit, name="admin_yacht_edit"),
    path('yacht/delete/<pk>', views.yacht_delete, name="admin_yacht_delete"),

    # Employees
    path('employees/', views.employee_list, name="admin_employee_list"),
    path('employees/add', views.employee_add, name="admin_employee_add"),
    path('employees/edit/<email>', views.employee_edit, name="admin_employee_edit"),
    path('employees/delete/<email>', views.employee_delete, name="admin_employee_delete"),

    # Package
    path('package/', views.package_list, name="admin_package_list"),
    path('package/add', views.package_add, name="admin_package_add"),
    path('package/edit/<pk>', views.package_edit, name="admin_package_edit"),
    path('package/delete/<pk>', views.package_delete, name="admin_package_delete"),

    # Event
    path('event/', views.event_list, name="admin_event_list"),
    path('event/add', views.event_add, name="admin_event_add"),
    path('event/edit/<pk>', views.event_edit, name="admin_event_edit"),
    path('event/delete/<pk>', views.event_delete, name="admin_event_delete"),
    path('event/bookings', views.event_booking, name="admin_event_booking_list"),

    # Training
    path('training/', views.training_list, name="admin_training_list"),
    path('training/add', views.training_add, name="admin_training_add"),
    path('training/edit/<pk>', views.training_edit, name="admin_training_edit"),
    path('training/delete/<pk>', views.training_delete, name="admin_training_delete"),
    path('training/bookings', views.training_booking, name="admin_training_booking_list"),

    # YACHT PACKAGE Booking
    path('bookings/', views.booking, name="admin_bookings"),

    # Feedback
    path('feedbacks/', views.feedback, name="admin_feedback")
]
