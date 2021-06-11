from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

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


class HomePageView(View):
    template_name = "core/homepage.html"

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Home | Flash Forum"
        }
        return render(request, self.template_name, context)