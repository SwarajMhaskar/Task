from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_table, name='display_table'),
    path('selected_row/<int:row_id>/', views.display_selected_row, name='display_selected_row'),
    path('add_row/', views.add_row, name='add_row'),
]
