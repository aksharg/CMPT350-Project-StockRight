# Generated by Django 3.0.4 on 2020-04-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockQuotes', '0003_auto_20200331_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]