from django.urls import path
from . import views

app_name = 'coupon_usage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
