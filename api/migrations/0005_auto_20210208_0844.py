# Generated by Django 3.1.1 on 2021-02-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210207_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
