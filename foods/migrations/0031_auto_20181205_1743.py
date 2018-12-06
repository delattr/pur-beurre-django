# Generated by Django 2.1.2 on 2018-12-05 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0030_auto_20181205_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='last_modified_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
