from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('note/<int:pk>/', views.note, name='note'),
    path('add/', views.add_note, name='add_note'),
    path('<str:pk>', views.delete_note, name='delete_note'),
    path('update/<str:pk>', views.update_note, name='update_note'),
    path('search/', views.search, name='search'),
    path('search/<str:pk>', views.search_note, name='search_note'),
]
