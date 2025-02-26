<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-01-28 11:40
=======
# Generated by Django 5.1.4 on 2025-01-22 03:00
>>>>>>> 6b2e3bd1e212ea7a3d823cbdd13bc045dadcc523

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='BottleSpin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('option', models.CharField(blank=True, choices=[('UP', 'UP'), ('DOWN', 'DOWN')], max_length=50, null=True)),
                ('outcome', models.CharField(blank=True, choices=[('UP', 'UP'), ('DOWN', 'DOWN')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('LOSS', 'LOSS'), ('WON', 'WON')], default='PENDING', max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('multiplier', models.FloatField(default=1.0)),
                ('claimed', models.BooleanField(default=False)),
                ('bomb_card', models.JSONField()),
                ('active', models.BooleanField(default=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeadorTail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.IntegerField(default=0)),
                ('winnings', models.IntegerField(default=0)),
                ('option', models.CharField(blank=True, choices=[('HEAD', 'HEAD'), ('TAIL', 'TAIL')], max_length=50, null=True)),
                ('outcome', models.CharField(blank=True, choices=[('HEAD', 'HEAD'), ('TAIL', 'TAIL')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('LOSS', 'LOSS'), ('WON', 'WON')], default='PENDING', max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Minislot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.CharField(max_length=244)),
                ('result2', models.CharField(max_length=244)),
                ('result3', models.CharField(max_length=244)),
                ('stake', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
=======
            name='Minislot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.CharField(max_length=20)),
                ('result2', models.CharField(max_length=20)),
                ('result3', models.CharField(max_length=20)),
                ('stake', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
>>>>>>> 6b2e3bd1e212ea7a3d823cbdd13bc045dadcc523
                ('status', models.CharField(choices=[('WON', 'WON'), ('LOSS', 'LOSS'), ('PENDING', 'PENDING')], default='PENDING', max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='RockPapperSissors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('option', models.CharField(blank=True, choices=[('ROCK', 'ROCK'), ('PAPER', 'PAPER'), ('SISSORS', 'SISSORS')], max_length=50, null=True)),
                ('outcome', models.CharField(blank=True, choices=[('ROCK', 'ROCK'), ('PAPER', 'PAPER'), ('SISSORS', 'SISSORS')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('LOSS', 'LOSS'), ('WON', 'WON'), ('DRAW', 'DRAW')], default='PENDING', max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
=======
>>>>>>> 6b2e3bd1e212ea7a3d823cbdd13bc045dadcc523
    ]
