# Generated by Django 3.1.1 on 2021-02-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_student_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='finish',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='student',
            name='position',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]