# Generated by Django 5.1.4 on 2025-01-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_deposit_reference_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference_number',
            field=models.CharField(default='n2CvPPB4ExEJAAivSYWZ', max_length=50),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference_number',
            field=models.CharField(default='FFuWszp9k0fOs2F0vL1k', max_length=50),
        ),
    ]
