from django.urls import path
from . import views

urlpatterns = [
    path('', views.balance_sheet_view, name='balance_sheet'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
]
