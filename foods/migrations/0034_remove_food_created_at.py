# Generated by Django 2.1.2 on 2018-12-06 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0033_food_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='created_at',
        ),
    ]
