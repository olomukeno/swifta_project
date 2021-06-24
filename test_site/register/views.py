import os
from time import sleep

from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import *
from .models import Profile, User
from django.contrib import messages


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(response.POST)
        if form.is_valid():
            form.save()
            return render(response, "registration/redirect.html", {})
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form": form})


def login(response):
    if response.method == 'POST':
        form = AuthenticationForm(response.POST)
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(response, user)
                messages.success(response, 'Logged in successfully')
                sleep(2)
                return redirect('index')
        else:
            messages.error(response, 'Incorrect Username or Password')
            return redirect('/login')

    else:
        form = AuthenticationForm()
    return render(response, 'registration/login.html', {'form': form})


def log_out(response):
    # if user.is_authenticated:
    # if response.method == "POST":
    logout(response)
    # return render(response, 'registration/logged_out.html', {})
    return redirect('/login')


# @transaction.atomic
def update_profile(response):
    user = User.objects.get(username=response.user.username)
    profile = Profile.objects.get(user=user)
    # profile.first_name = response.POST.get("first_name")
    # profile.last_name = response.POST.get("last_name")
    # profile.user.birthday = response.POST.get("birthday")
    # profile.gender = response.POST.get("gender")
    print(profile.first_name)
    print(profile.last_name)
    print(profile.birthday)
    print(profile.gender)
    print(profile.avatar)
    # print(profile.avatar)
    # profile.get_full_name()
    # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'

    # profile.avatar = response.FILES.get("avatar")

    if response.method == 'POST' and response.POST.get("update"):
        data = ["first_name", "last_name", "birthday", "gender"]
        for value in data:
            if len(str(response.POST.get(value))) > 0:
                if value == "first_name":
                    profile.first_name = response.POST.get(value)
                elif value == "last_name":
                    profile.last_name = response.POST.get(value)
                elif value == "birthday":
                    profile.birthday = response.POST.get(value)
                elif value == "gender":
                    if response.POST.get(value).isdigit():
                        profile.gender = response.POST.get(value)
                profile.save()
        if response.FILES.get("avatar") is not None:
            print(len(str(response.FILES.get("avatar"))))
            print(str(response.FILES.get("avatar")))
            # if len(str(profile.avatar)) > 0:
                # os.remove(str(profile.avatar))
                # print(os.path.join(MEDIA_ROOT,  str(profile.avatar)))
            profile.avatar = response.FILES.get("avatar")
            profile.save()
        # myfile = response.FILES['file']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        return render(response, 'registration/profile.html', {"profile": profile})
    # else:
    #     form = ProfileForm()
    #
    return render(response, 'registration/profile.html', {"profile": profile})
    # return render(response, 'core/simple_upload.html')
# def profile(response):
#     if response.method == 'POST':
#         print(response.POST)
#         print(response.POST.get("username"))
#         # profile
#         print(UserProfile.objects.all())
#         # user_form = UserForm(response.POST, instance=response.user)
#         # profile_form = ProfileForm(response.POST, instance=response.user.profile)
#     #     if profile_form.is_valid():
#     #         # if user_form.is_valid() and profile_form.is_valid():
#     #         # user_form.save()
#     #         profile_form.save()
#     #         messages.success(response, 'Your profile was successfully updated!')
#     #         return redirect('settings:profile')
#     #     else:
#     #         messages.error(response, 'Please correct the error below.')
#     # else:
#     #     # user_form = UserForm(instance=request.user)
#     #     # profile_form = ProfileForm(instance=response.user.profile)
#         return render(response, 'registration/profile.html', {"profile": profile})


#
#
