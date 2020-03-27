# Generated by Django 3.0.3 on 2020-03-27 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesApp', '0007_auto_20200320_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_repair',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='repair',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]