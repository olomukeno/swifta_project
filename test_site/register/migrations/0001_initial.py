# Generated by Django 3.2.3 on 2021-06-16 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='customers/profiles/avatars/')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
