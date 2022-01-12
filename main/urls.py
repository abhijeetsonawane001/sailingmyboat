from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('login', views.login_view, name='main_login'),
    path('logout', views.logout_view, name='main_logout'),
    path('create-account', views.create_account, name="main_create_account"),

    # Yacht detail
    path('yacht/detail/<pk>', views.yacht_detail, name='main_yacht_detail'),

    # Events
    path('events', views.events_list, name="main_event_list"),
    path('events/detail/<pk>', views.events_detail, name='main_event_detail'),
    path('events/register/<event_id>', views.event_booking, name="main_event_register"),

    # Trainings
    path('trainings', views.trainings_list, name="main_training_list"),
    path('trainings/detail/<pk>', views.trainings_detail, name='main_training_detail'),
    path('trainings/register/<training_id>', views.training_booking, name="main_training_register"),

    # Packages
    path('packages', views.package_list, name="main_package_list"),
    path('packages/detail/<pk>', views.package_detail, name="main_package_detail"),

    # Booking
    path('booking', views.booking, name="main_booking"),
    path('booking/success', views.success, name="main_booking_success"),

    path('feedback', views.feedback, name="main_feedback")
]
