# Generated by Django 2.1.2 on 2018-12-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0028_auto_20181205_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='last_modified_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='staging',
            name='last_modified_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
