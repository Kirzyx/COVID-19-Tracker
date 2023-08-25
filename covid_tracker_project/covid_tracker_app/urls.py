from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('display/', views.display_all_entries, name='display_entries'),
    path('remove/<str:country_name>/', views.remove_entry, name='remove_entry'),
    path('get/<str:country_name>/', views.get_entry, name='get_entry'),
]
