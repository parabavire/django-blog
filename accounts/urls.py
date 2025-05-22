from django.urls import path
from .views import SignUpVew

urlpatterns = [
    path("signup/", SignUpVew.as_view(), name="signup"),
]