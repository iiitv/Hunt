# Generated by Django 3.1.1 on 2021-02-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
