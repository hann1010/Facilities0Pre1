# Generated by Django 3.0.3 on 2020-05-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesApp', '0026_auto_20200521_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_repair',
            field=models.DateField(blank=True),
        ),
    ]