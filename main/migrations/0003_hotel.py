# Generated by Django 4.0.1 on 2022-03-10 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_destination_id_alter_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('Food_price', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField(blank=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.destination')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
