# Generated by Django 5.1.4 on 2025-01-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_deposit_reference_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference_number',
            field=models.CharField(default='vHK3HgA7enZITycjaCu3', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference_number',
            field=models.CharField(default='NpLRwnIbtgPKZheIgVVm', max_length=50),
        ),
    ]