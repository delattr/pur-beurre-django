# Generated by Django 2.1.2 on 2018-11-30 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0012_auto_20181130_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foods',
            old_name='categories_tag',
            new_name='categories_tags',
        ),
    ]