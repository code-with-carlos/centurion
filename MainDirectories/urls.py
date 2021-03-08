from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.DataOwnerHomeView.as_view(), name='data_owner_home'),
  
]