# Generated by Django 3.1.1 on 2021-02-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210217_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='banned',
            field=models.IntegerField(default=1),
        ),
    ]