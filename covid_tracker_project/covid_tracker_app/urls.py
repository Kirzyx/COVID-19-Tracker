from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('display/', views.display_all_entries, name='display_entries'),
    path('remove/<str:country_name>/', views.remove_entry_page, name='remove_entry'),
    path('remove-entry-page/', views.remove_entry_page, name='remove_entry_page'),
    path('get-entry-page/', views.get_entry_page, name='get_entry_page'),
    path('get/<str:country_name>/', views.display_country_details, name='display_country_details'),
    path('', views.index, name='index'),
    path('country-summary/', views.display_country_summary, name='country_summary'),
]
