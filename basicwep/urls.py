from django.urls import include, path
from basicwep import views


urlpatterns = [
    path("", views.home),
]
