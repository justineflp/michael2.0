from django.urls import path
from . import views

app_name = 'report_ticket'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
