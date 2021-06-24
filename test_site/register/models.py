from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext
import os
from uuid import uuid4


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    avatar = models.ImageField(upload_to="profile/", default="profile/Cover.jpg", null=True, blank=False)
    birthday = models.DateField(null=True)
    # img_pic = models.ImageField()
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CUSTOM = 3
    GENDER_CHOICES = [
        (GENDER_MALE, gettext("Male")),
        (GENDER_FEMALE, gettext("Female")),
        (GENDER_CUSTOM, gettext("Custom")),
    ]

    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True)

    def get_full_name(self):
        return str(self.last_name) + " " + str(self.first_name)


    def rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper