from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("<int:month>", views.numeric_month),
    path("<str:month>", views.month1 ,name = "monthly_challenge")
]
