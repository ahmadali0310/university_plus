# Generated by Django 3.1.2 on 2020-12-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cnic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='w_number',
            field=models.IntegerField(),
        ),
    ]