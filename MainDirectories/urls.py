from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.DataOwnerHomeView.as_view(), name='data_owner_home'),
    path('files/', views.DataFileListView.as_view(), name='data_file_list'),
    path('files/upload/', views.DataFileUploadView.as_view(), name='data_file_create'),
]