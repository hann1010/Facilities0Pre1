# Generated by Django 3.0.3 on 2020-03-27 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesApp', '0012_auto_20200327_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_repair',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
