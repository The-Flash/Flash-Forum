from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
def sign_out(request):
    logout(request)
    return redirect(reverse("core:sign-in"))

class SignInView(View):
    template_name = "core/sign-in.html"

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Sign In | Flash Forum"
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect(reverse("core:homepage"))
        messages.add_message(request, messages.ERROR, "Incorrect credentials!")
        return redirect(reverse("core:sign-in"))


class SignUpView(View):
    template_name = "core/sign-up.html"

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Sign Up | Flash Forum"
        }
        return render(request, self.template_name, context)


class HomePageView(LoginRequiredMixin, View):
    template_name = "core/homepage.html"
    redirect_field_name = "next"

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Home | Flash Forum"
        }
        return render(request, self.template_name, context)

    def get_login_url(self):
        return reverse("core:sign-in")