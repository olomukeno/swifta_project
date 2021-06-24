from django.urls import path
from . import views

# from '.' means the current directory

urlpatterns = [
    # from the project's urls.py file it navigates back to here and with it looks that the first parameter to look for
    # the correct path it was given and subsequently direct it to the required function
    path("", views.index, name="index"),
    path("home/", views.test2, name="test"),
    path("<int:ind>", views.index2, name="index2"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("view2/", views.view2, name="view2"),
    # path("profile/", views.profile, name="profile"),
    # this means it is going to look for any integer located in the path given
    # str can also be used here
]
