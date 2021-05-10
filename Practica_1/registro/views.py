from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User
from main import views as mv
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from django.db import models
# Create your views here.
from .models import Profile
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile.objects.get_or_create(user=user, profesion=form.cleaned_data['profesion'], cui=form.cleaned_data['cui'])
            return redirect(reverse('profile', kwargs={'nom':user.username}))

    else:
        form = RegisterForm()

    return render(request, 'registro/registro.html', {'form':form})


class Inicio(LoginView):

    def get_new_url(self):

        return str(self.request.user)

def profile(request, username):
    if request.user.is_authenticated and request.user.username == username:
        if request.method == 'POST':
            p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
            u_form = UserUpdateForm(request.POST,instance=request.user)
            if p_form.is_valid() and u_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request,'Su usuario ha sido actualizado.')
                return redirect('profile')
        else:
            p_form = ProfileUpdateForm(instance=request.user)
            u_form = UserUpdateForm(instance=request.user.profile)

        context={'p_form': p_form, 'u_form': u_form}
        return render(request, 'registro/profile.html',context )