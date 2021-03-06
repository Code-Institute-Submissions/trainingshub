from django.urls import path
from . import views


urlpatterns = [
    path("signuplist/coming/", views.signup_list, name="signuplist"),
    path("signuplist/completed/", views.signup_list_completed, name="signuplist-completed"),
    path("signup-detail/<id>/", views.signup_detail, name="signup-detail"),
    path("<id>/", views.signup, name="signup"),
    path("<id>/checkout/", views.checkout, name="checkout"),
]
