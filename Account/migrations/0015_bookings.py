# Generated by Django 4.0.5 on 2023-04-05 18:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0014_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('BookingId', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
                ('sno', models.IntegerField()),
                ('price', models.IntegerField()),
                ('booking_date', models.DateField(default=datetime.datetime.today)),
                ('service_date', models.DateField()),
                ('slote', models.CharField(max_length=20)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
