from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.getContacts),
    path('save/', views.saveContacts),
    path('view/<int:id>/', views.getContact),
    path('delete/<int:id>/', views.deleteContact),
    path('edit/<int:id>/', views.updateContact)

]