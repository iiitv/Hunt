# Generated by Django 3.1.1 on 2020-12-16 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('level_number', models.IntegerField(unique=True)),
                ('link', models.URLField()),
                ('score', models.IntegerField()),
                ('decay', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('current_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.level')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]
