# Generated by Django 2.1.2 on 2018-11-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_auto_20181130_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='brands',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='product_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='quantity',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
