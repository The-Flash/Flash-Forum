from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("", views.HomePageView.as_view(), name="homepage")
]