# Generated by Django 3.0.3 on 2020-03-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesApp', '0013_auto_20200327_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='received',
            field=models.BooleanField(default='false'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='repair_state',
            field=models.BooleanField(default='false'),
        ),
    ]