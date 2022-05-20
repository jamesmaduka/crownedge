# Generated by Django 4.0.3 on 2022-05-11 11:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_payment_admin_note_payment_admin_upadate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='del_booking',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='admin_upadate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
