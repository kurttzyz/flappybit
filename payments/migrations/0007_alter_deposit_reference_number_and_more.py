<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-01-22 03:10
=======
# Generated by Django 5.1.4 on 2025-01-12 04:24
>>>>>>> 0244ff341220a700c22737e2212fae206c843efa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_deposit_reference_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference_number',
<<<<<<< HEAD
            field=models.CharField(default='LAa4cBaTxRyVNMK7MAT9', max_length=50),
=======
            field=models.CharField(default='5etG4hTjZskUSs1TBeDc', max_length=50),
>>>>>>> 0244ff341220a700c22737e2212fae206c843efa
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference_number',
<<<<<<< HEAD
            field=models.CharField(default='QS7P528N76v2ZAGcv6cI', max_length=50),
=======
            field=models.CharField(default='bbZI7I4R44hc9zOwibiC', max_length=50),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
>>>>>>> 0244ff341220a700c22737e2212fae206c843efa
        ),
    ]
