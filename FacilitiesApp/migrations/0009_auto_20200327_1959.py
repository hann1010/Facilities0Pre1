# Generated by Django 3.0.3 on 2020-03-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesApp', '0008_auto_20200327_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='repair_state',
            field=models.BooleanField(default='False'),
        ),
    ]
