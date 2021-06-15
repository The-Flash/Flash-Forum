from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def sign_out(request):
    logout(request)
    return redirect(reverse("core:sign-in"))

class SignInView(View):
    template_name = "core/sign-in.html"
    context = {
        "title": "Sign In | Flash Forum"
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

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
    context = {
        "title": "Sign Up | Flash Forum"
    }

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("core:complete-profile")
        self.context["form"] = form
        return render(request, self.template_name, self.context)


class CompleteProfileView(LoginRequiredMixin, View):
    template_name = "core/complete-profile.html"
    login_url = reverse_lazy("core:sign-in")
    context = {
        "title": "Complete Profile | Flash Forum"
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class HomePageView(LoginRequiredMixin, View):
    template_name = "core/homepage.html"
    login_url = reverse_lazy("core:sign-in")
    context = {
        "title": "Home | Flash Forum"
    }

    def get(self, request, *args, **kwargs):  
        return render(request, self.template_name, self.context)
