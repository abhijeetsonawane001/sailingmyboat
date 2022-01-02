from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='admin_dashboard'),
    # Yachts
    path('yacht/types', views.yacht_type_list, name='admin_yacht_type_list'),
    path('yacht/types/add', views.yacht_type_add, name='admin_yacht_type_add'),
    path('yacht/types/edit/<slug>', views.yacht_type_edit, name="admin_yacht_type_edit"),
    path('yacht/types/delete/<slug>', views.yacht_type_delete, name="admin_yacht_type_delete"),
]
