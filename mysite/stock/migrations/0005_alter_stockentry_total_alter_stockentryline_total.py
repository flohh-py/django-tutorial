# Generated by Django 4.0.2 on 2022-02-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_stockentryline_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockentry',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='stockentryline',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
