# Generated by Django 2.1.2 on 2018-12-05 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0029_auto_20181205_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
