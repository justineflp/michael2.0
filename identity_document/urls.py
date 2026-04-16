from django.urls import path
from . import views

app_name = 'identity_document'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
