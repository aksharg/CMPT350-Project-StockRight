# Generated by Django 3.0.4 on 2020-04-01 05:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockQuotes', '0004_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='buyPrice',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='stock',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
