# Generated by Django 4.0.3 on 2022-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_booking_checkout_date_booking_future'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='checkout_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='checkout_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]