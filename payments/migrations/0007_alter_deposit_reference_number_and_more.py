# Generated by Django 5.1.4 on 2025-02-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_deposit_reference_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference_number',
            field=models.CharField(default='4YAtSDhlVud9ZLY4jFdL', max_length=50),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference_number',
            field=models.CharField(default='fRGAZVH5GoEApzOroWwI', max_length=50),
        ),
    ]
